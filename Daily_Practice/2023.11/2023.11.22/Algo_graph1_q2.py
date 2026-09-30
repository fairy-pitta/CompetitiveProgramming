
def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
    for i in range(N):
        ans = sorted(G[i])
        print(*ans)

main()
