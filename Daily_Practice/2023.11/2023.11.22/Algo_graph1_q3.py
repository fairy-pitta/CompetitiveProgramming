
def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    G_length = [(0) for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
        G_length[a] = len(G[a])
        G_length[b] = len(G[b])
    
    max_friends = max(G_length)
    
    for i in range(N):
        if len(G[i]) == max_friends:
            ans = sorted(G[i])
            print(*ans)
            break

main()
    
    
    
    
    