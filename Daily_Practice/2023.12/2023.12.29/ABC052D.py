N, A, B = map(int, input().split())
X = list(map(int, input().split()))
cost = 0
for i in range(1, N):
    if (X[i] - X[i-1])*A > B:
        cost += B
    else:
        cost += (X[i] - X[i-1])*A

print(cost)
