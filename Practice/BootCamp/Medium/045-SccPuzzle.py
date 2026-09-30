
def main():
    N, M = map(int, input().split())
    ans = 0

    if N*2 <= M:
        ans += N
        M -= N*2
    else:
        print(M//2)
        return 
    
    ans += M//4

    print(ans)

main()