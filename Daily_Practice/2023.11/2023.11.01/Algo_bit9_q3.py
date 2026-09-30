
def main():
    N, K = map(int, input().split())
    v = list(map(int, input().split()))

    ans = 0

    for i in range(K):
        ans += (1<<v[i])
    
    print(ans)

main()

