N, A = map(int, input().split())
T = list(map(int, input().split()))

cur = 0

for i in T:
    if i >= cur:
        cur = i + A
        print(cur)
    else:
        print(cur + A)
        cur += A

