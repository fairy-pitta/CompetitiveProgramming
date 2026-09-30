N = int(input())
A = list(map(int, input().split()))

def calc_divisors(N) -> list:
    res = []

    for i in range(1, N+1):
        if i * i > N:
            break 

        if N % i != 0:
            continue 

        res.append(i)

        if N // i != i:
            res.append(N // i)
    
    res.sort()

    return res 

from collections import defaultdict

d = defaultdict(int)

for i in A:
    d[i] += 1

ans = 0
for j in range(N):
    li = calc_divisors(A[j])
    # print(li)
    for k in li:
        if d[k] and d[A[j]//k]:
            ans += d[k] * d[A[j]//k]

print(ans)

