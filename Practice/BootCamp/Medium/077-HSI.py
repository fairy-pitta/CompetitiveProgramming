def main():
    N, M = map(int, input().split())
    time_per_submission = 1900 * M + 100 * (N-M)
    ans = time_per_submission * 2 ** M
    print(ans)

main()
