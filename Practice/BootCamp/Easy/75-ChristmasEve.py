
def main():
    N, K = map(int, input().split())
    h = []
    for _ in range(N):
        h.append(int(input()))
    
    h = sorted(h)

    ans = 10**19
    for min_h in range(N-K+1):
        ans = min(ans, h[min_h+K-1]-h[min_h])
    
    print(ans)


main()