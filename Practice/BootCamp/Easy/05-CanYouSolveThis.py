
def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    ans = 0
    for _ in range(N):
        a = list(map(int, input().split()))
        score = C
        for i in range(M):
            score += a[i]*B[i]
        if score > 0:
            ans += 1
    
    print(ans)

main()