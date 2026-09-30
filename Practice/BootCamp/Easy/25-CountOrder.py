from itertools import permutations 
from bisect import bisect_right

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))

    N_perm = sorted(permutations(P))
    P_idx = bisect_right(N_perm, tuple(P))
    Q_idx = bisect_right(N_perm, tuple(Q))
    print(abs(P_idx-Q_idx))

main()


