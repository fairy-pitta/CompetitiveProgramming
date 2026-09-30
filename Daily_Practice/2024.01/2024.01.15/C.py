# 10進法をn進法に変換する
def base10to(n, b):
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)

N = int(input())
S = base10to(N-1, 5)
ans = ""
for i in S:
    k = int(i)
    ans += str(k*2)
print(ans)