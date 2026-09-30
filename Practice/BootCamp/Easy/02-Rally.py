
def main():
    N = int(input())
    X = list(map(int, input().split()))
    ans = 10**18
    for meeting_place in range(max(X)+1):
        power_needed = 0
        for person in range(N):
            power_needed += (X[person] - meeting_place)**2
            
        ans = min(ans, power_needed)
    
    print(ans)

main()

