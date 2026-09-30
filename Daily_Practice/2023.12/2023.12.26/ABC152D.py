
def main():
    N = int(input())
    cnt = [[(0) for _ in range(10)] for _ in range(10)]
    for i in range(1, N+1):
        head = int(str(i)[0])
        tail = int(str(i)[-1])
        cnt[head][tail] += 1
    
    ans = 0
    for h in range(10):
        for t in range(10):
            ans += cnt[h][t] * cnt[t][h]
    

    print(ans)

main()