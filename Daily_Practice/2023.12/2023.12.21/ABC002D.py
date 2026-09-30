def main():
    N, M = map(int, input().split())
    G = [set() for i in range(N+1)]
    for _ in range(M):
        x, y = map(int, input().split())
        G[x].add(y)
        G[y].add(x)
    
    ans = 0
    print(G)
    for i in range(len(G)):
        l = len(list(G[i]))
        cnt = 0
        for j in range(len(G)):
            if i == j:
                continue
            if G[i] == G[j]:
                cnt += 1
        if cnt == l:
            ans = max(cnt, ans)
    
    print(ans+1)
main()