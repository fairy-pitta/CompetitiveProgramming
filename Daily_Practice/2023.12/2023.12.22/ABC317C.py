from itertools import permutations 

def main():
    N, M = map(int, input().split())
    cities = list(permutations(range(N)))
    A = [[(0) for _ in range(N)] for _ in range(N)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        A[a-1][b-1] = c
        A[b-1][a-1] = c
    
    ans = 0
    
    for choice in cities:
        dist = 0
        for i in range(N-1):
            if A[choice[i]][choice[i+1]] == 0:
                break
            dist += A[choice[i]][choice[i+1]]
        ans = max(ans, dist)
    
    print(ans)

main()
        





    