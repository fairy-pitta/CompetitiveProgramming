from collections import defaultdict 
from sortedcontainers import SortedSet
MOD = 2**20
def main():
    Q = int(input())
    A = [(-1) for _ in range(2**20)]
    S = SortedSet(range(1, 2**20+1))
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 2:
            print(A[x%MOD-1])
        else:
            h = x
            if len(S) == 2**20:
                while True:
                    if A[h%MOD-1] == -1:
                        A[h%MOD-1] = x
                        break
                    h += 1
                S.discard(h%MOD)
            else:
                A[S.pop(0)-1] = x
    

main()



