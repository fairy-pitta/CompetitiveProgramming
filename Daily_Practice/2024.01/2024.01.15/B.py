def base10to(n, b):
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)

N = int(input())
S = base10to(N, 2)

ans = 0
for i in reversed(list(S)):
    if i == "0":
        ans += 1
    else:
        break

print(ans)