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

def main():
    A = int(input())
    N = 1

    li = factorize(A)
    for i in range(len(li)):
        factor, num = li[i][0], li[i][1]
        if num % 2 == 1:
            N *= factor 
    
    return N

print(main())