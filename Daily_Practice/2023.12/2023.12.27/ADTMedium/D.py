def main():
    N = int(input())
    from collections import defaultdict 
    d = defaultdict(list)
    cnt = [(0) for _ in range(N+1)]
    for i in range(1, N+1):
        c = int(input())
        cnt[i] = c
        li = list(map(int, input().split()))
        for j in li:
            d[j].append(i)
    
    X = int(input())
    winner = []
    for i in d[X]:
        winner.append([cnt[i], i])
    
    winner = sorted(winner)
    ans = []
    for k in winner:
        if k[0] == winner[0][0]:
            ans.append(k[1])
    
    print(len(ans))
    print(*ans)

main()

