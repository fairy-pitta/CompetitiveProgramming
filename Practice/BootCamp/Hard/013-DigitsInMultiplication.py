N = int(input())

ans = 10**18

for i in range(1, int(N**0.5)+1):
    if N % i == 0:
        f = str(i)
        s = str(N//i)
        ans = min(ans, max(len(f), len(s)))

print(ans)
