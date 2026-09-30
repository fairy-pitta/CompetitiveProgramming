
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
    
    # a multiset version of the SortedSet. 
    # it can contain multiple same leafs 

    # SortedMultiSet(a = []) : create SotedMultiSet from iterable. 
    # No overlaps and sorted 

    # s.a : show the content of the SortedSet 

    # len(s) : returns the number of leafs in the set 

    # x in s / x not in s : return a boolean 

    # s.add(x) : if x is not in s then add x and returns True 

    # s.discard(x) : if x in s then delete x and return True

    # s.lt(x) / s.le(x) / s.gt(x) / s.ge(x) : returns a min/max leaf that is less/greater than/or equal to x.
    # if such leaf does not exist, return None

    # s[x] : indexing 

    # s.index[x]: if x in s then returns the index of x 

    # s.index_right[x] : index but right 


    # add-ons 

    # s.add(x) : adds x to s whether or not x is in s 

    # s.discard(x) : delete x once if x in s and returns True 

    # s.count(x) : count the number of x in s 
# Input 
# Q
# query 1 
# query 2 
# query q 

# 1 x: add x to the list 
# 2 x k: for elements less than x in the list, output k-th biggest element 
# 3 x k: for elements more than x in the list, output k-th smallest element 
# if less than k elements that are more than x in the list, output -1 

def solve():
    A = SortedMultiset()
    Q = int(input())
    for _ in range(Q):
        S = list(map(int, input().split()))

        if S[0] == 1:
            A.add(S[1])

        elif S[0] == 2:
            cnt = A.index_right(S[1])
            if cnt >= S[2]:
                print(A[cnt - S[2]])
            else:
                print("-1")

        else:
            less_than_x = A.index(S[1])
            more_than_x = len(A) - less_than_x
            # print("this is right index", cnt)
            if more_than_x >= S[2]:
                print(more_than_x - S[2] + less_than_x -1)
            else:
                print("-1")
        # print(A)
        
solve()

             




