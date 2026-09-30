def my_ceil(N, W):
    return (-(-N//W))

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    ans = my_ceil(N-1, K-1)
    print(ans)

main()
