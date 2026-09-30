N = str(input())

l = len(N)

MOD = 998244353

res = int(N) % MOD

pmd = pow(10, l * int(N), MOD)
imd = pow(1 - pow(10, l, MOD), -1, MOD)

ans = (int(N) * (1-pmd)*imd) % MOD

print(ans)
