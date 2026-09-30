def main():
    N = int(input())
    A = list(map(int, input().split()))
    
    ans = 10**18
    for i in range(min(A), max(A)+1):
        cost = 0
        for j in range(N):
            cost += abs(i-A[j])**2
        ans = min(ans, cost)
    
    print(ans)

main()