
def main():
    N = int(input())
    K = int(input())
    x = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += min(x[i], abs(x[i]-K))*2
    print(ans)

main()

