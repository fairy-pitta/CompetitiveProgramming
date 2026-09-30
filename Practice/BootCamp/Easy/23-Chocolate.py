from math import ceil
def main():
    N = int(input())
    D, X = map(int, input().split())
    ans = X
    for _ in range(N):
        a = int(input())
        ans += ceil(D/a)
    
    print(ans)

main()
