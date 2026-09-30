def main():
    N, M = map(int, input().split())
    max_l = 0
    min_r = 10**18
    for _ in range(M):
        l, r = map(int, input().split())
        max_l = max(max_l, l)
        min_r = min(min_r, r)

    if max_l > min_r:
        print(0)
    else:
        print(min_r-max_l+1)

main()
