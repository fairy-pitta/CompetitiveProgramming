def main():
    T = int(input())

    def solve(N):
        # 一番近いその数より小さい平方数を見つける
        sq = 1
        ans = 0
        while True:
            if sq ** 2 > N:
                sq -= 1
                break
            else:
                sq += 1

        if N == sq ** 2:
            ans = (sq - 1) * sq * 2 
        elif N - sq**2 == 1:
            ans = (sq - 1) * sq * 2 + 1 
        elif N - sq**2 == sq:
            ans = sq * sq * 2 + 1
        elif N - sq**2 == sq+1:
            ans = sq * sq * 2 + 2
        elif N - sq**2 < sq:
            rem = N - sq**2
            ans = ans = (sq - 1) * sq * 2 + 1 + (rem-1) * 2
        else:
            rem = N - sq**2
            ans = (sq - 1) * sq * 2 + 2 + (rem-2) * 2

        return ans 

    for _ in range(T):
        N = int(input())
        print(solve(N))

main()

