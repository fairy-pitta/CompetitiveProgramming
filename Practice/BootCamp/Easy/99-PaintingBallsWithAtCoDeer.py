def main():
    N, K = map(int, input().split())
    ans = K
    for i in range(1, N):
        ans *= (K-1)
    
    print(ans)
main()