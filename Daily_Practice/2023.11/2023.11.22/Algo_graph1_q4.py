
def main():
    N, M, X = map(int, input().split())
    G = [set() for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].add(b)
        G[b].add(a)
    
    ans = set()

    for friend in G[X]:
        for friend_of_friend in G[friend]:
            if X not in G[friend_of_friend]:
                ans.add(friend_of_friend)
    # print(ans)
    if X in ans:
        print(len(ans)-1)
    else:
        print(len(ans))

main()
                