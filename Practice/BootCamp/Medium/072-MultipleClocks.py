from math import lcm 
from functools import reduce 

def main():
    N = int(input())
    t = [int(input()) for _ in range(N)]
    ans = reduce(lcm, t)
    print(ans)

main()