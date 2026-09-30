N = int(input())
P = []
A = []

for _ in range(N):
    p, a = map(int, input().split())
    P.append(p)
    A.append(a)

dp = [[(0) for _ in range(N)] for _ in range(N)]
dp[0][-1] = 0

print(P)
print(A)

for gap in reversed(range(0, N-1)):
    for l in range(N-gap):
        r = l + gap
        
        # l-1番目のブロックを取り除くときの得点
        score1 = A[l-1]
        if l >= 2 and l <= P[l-1] <= r:
            print(l, r, gap)

