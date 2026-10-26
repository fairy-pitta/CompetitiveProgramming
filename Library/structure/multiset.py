"""SortedMultiset: 同じ値を何個でも入れられる、常にソートされた多重集合。

    s = SortedMultiset([3, 1, 4, 1, 5])   # {1, 1, 3, 4, 5} (重複もそのまま持つ)
    s.add(1)                               # {1, 1, 1, 3, 4, 5}。戻り値は無し
    s.count(1)         ->  3
    s.discard(1)                           # True。1 を「1 個だけ」消す
    s.ge(2)            ->  3               # 2 以上で最小。無ければ None
    s[0], s[-1]        ->  1, 5            # 最小値・最大値

出典: tatyam さんの SortedMultiset (Unlicense) の旧版。下のコードは出典のまま。
https://github.com/tatyam-prime/SortedSet

sorted_set.py (SortedSet) との違い:
    - SortedSet      : 重複なし。add は「新しく入ったか」を True / False で返す
    - SortedMultiset : 重複あり。add は常に追加する (戻り値なし)。count(x) で個数がわかる
    「今いる人の点数の中央値 / 最大値を、出入りがあるたびに答える」のような、
    同じ値が何個も入りうる場面ではこちらを使う。

メソッド一覧 (計算量はすべて O(√N) 程度):
    len(s) / x in s / for x in s     : 要素数・存在判定・小さい順に列挙
    s.add(x)                         : x を 1 個追加 (既にあっても追加する)
    s.discard(x)                     : x を 1 個だけ削除。削除できたら True、無ければ False
    s.count(x)                       : x の個数
    s.lt(x) / s.le(x)                : x より小さい (以下の) 最大の要素。無ければ None
    s.gt(x) / s.ge(x)                : x より大きい (以上の) 最小の要素。無ければ None
    s[i]                             : 小さい方から i 番目 (0-indexed、負の数も可)
    s.index(x) / s.index_right(x)    : x 未満 / x 以下 の要素の個数

仕組み: SortedSet と同じ平方分割。ソート済みの短いリスト (バケット) を並べて持つ。
"""
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
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
        return "SortedMultiset" + str(self.a)
    
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

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

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
