# [[factor, time]]
def factorize(N) -> list:
    ans = []

    for p in range(2, N):
        # while p * p <= N
        if p * p > N:
            break 

        # if N cannot be divided by p
        # skip p
        if N % p != 0:
            continue 

        # power 
        e = 0
        while N % p == 0:
            e += 1
            N //= p

        ans.append([p, e])
    
    if N != 1:
        ans.append([N, 1])
    
    return ans 


N, M = map(int, input().split())
A = list(map(int, input().split()))
factors = set()
for i in A:
    li = factorize(i)
    for key, _ in li:
        factors.add(key)

ans = []
for i in range(1, M+1):
    flag = True
    li = factorize(i)
    for key, _ in li:
        if key in factors:
            flag = False 
    if flag:
        ans.append(i)

print(len(ans))
for k in ans:
    print(k)