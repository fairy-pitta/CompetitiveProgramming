
def main():
    N = int(input())
    F = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans |= (1<<F[i])
    
    print(ans)

main()