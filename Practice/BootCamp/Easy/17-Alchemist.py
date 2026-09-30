
def main():
    N = int(input())
    V = sorted(list(map(int, input().split())))
    ans = V[0]
    for i in range(1, N):
        ans = (ans+V[i])/2
    print(ans)

main()

