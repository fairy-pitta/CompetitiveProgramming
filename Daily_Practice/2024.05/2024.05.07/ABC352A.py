N, X, Y, Z = map(int, input().split())
ans = False
for station in range(min(X, Y), max(X, Y)+1):
    if station == Z:
        ans = True


if ans:
    print("Yes")
else:
    print("No")