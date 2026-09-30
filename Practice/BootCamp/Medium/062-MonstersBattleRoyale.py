from math import gcd
from functools import reduce
_=int(input())
print(reduce(gcd,list(map(int,input().split()))))


