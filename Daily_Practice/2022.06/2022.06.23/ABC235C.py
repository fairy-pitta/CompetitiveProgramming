from collections import defaultdict

def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    d = defaultdict(list)
    for ind in range(N):
        d[A[ind]].append(ind+1)
    # print(d)
    for _ in range(Q):
        x, k = map(int, input().split())
        # print(len(d[x]))
        if len(d[x]) >= k:

            print(d[x][k-1])
        else:
            print(-1)
    

main()
        
