
def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 10**18
    for i in range(N):
        num = A[i]
        cnt = 0
        while True:
            if num%2:
                break 
            num //= 2
            cnt += 1
        ans = min(ans, cnt)
    print(ans)
main()
