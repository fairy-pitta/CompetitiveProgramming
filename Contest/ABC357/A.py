N, M = map(int, input().split())
H = list(map(int, input().split()))

ans = 0

for i in range(N):
    if M < H[i]:
        break
    M -= H[i]
    ans += 1

print(ans)