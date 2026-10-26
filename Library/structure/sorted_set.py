"""SortedSet: 重複なしで常にソートされた集合。追加・削除・「x 以上で最小」の検索ができる。

    s = SortedSet([3, 1, 4, 1, 5])   # {1, 3, 4, 5} (重複は 1 つにまとまる)
    s.add(2)                          # True  (追加された)
    s.add(3)                          # False (もうある)
    s.discard(4)                      # True  (削除された)
    3 in s             ->  True
    s.ge(4)            ->  5          # 4 以上で最小。無ければ None
    s.lt(1)            ->  None       # 1 未満で最大。無ければ None
    s[0], s[-1]        ->  1, 5       # 小さい方から 0 番目、一番大きい要素
    s.index(3)         ->  2          # 3 未満の要素の数 (= 3 が何番目か)

出典: tatyam さんの SortedSet (Unlicense) の旧版。下のコードは出典のまま。
https://github.com/tatyam-prime/SortedSet

使い分け:
    - 同じ値を何個も入れたい → multiset.py (SortedMultiset)
    - 最小値の取り出しだけでよい → priority_queue.py (heapq) の方が速い
    - 標準の set は「x 以上で最小」を探せない。それが必要なときにこれを使う

メソッド一覧 (計算量はすべて O(√N) 程度):
    len(s) / x in s / for x in s     : 要素数・存在判定・小さい順に列挙
    s.add(x)                         : x を追加。追加できたら True、既にあれば False
    s.discard(x)                     : x を削除。削除できたら True、無ければ False
    s.lt(x) / s.le(x)                : x より小さい (以下の) 最大の要素。無ければ None
    s.gt(x) / s.ge(x)                : x より大きい (以上の) 最小の要素。無ければ None
    s[i]                             : 小さい方から i 番目 (0-indexed、負の数も可)
    s.index(x) / s.index_right(x)    : x 未満 / x 以下 の要素の個数

仕組み:
    1 本のソート済みリストに insert すると O(N) かかるので、長さ √N 程度の
    ソート済みリスト (バケット) を何本も並べて持つ (平方分割)。
    どのバケットに入るかを先頭から探し、そのバケットの中で bisect する。
    バケットが長くなりすぎたら全体を組み直す (_build)。

注意: 中身の数が 0 個のとき、ge / gt などは None を返す。None チェックを忘れないこと。
"""
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True
    
    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError
    
    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans
