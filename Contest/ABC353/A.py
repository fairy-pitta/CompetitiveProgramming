N = int(input())
H = list(map(int, input().split()))

base = H[0]
ans = -1

for i in range(1, N):
    if H[i] > base:
        ans = i+1
        break

print(ans)