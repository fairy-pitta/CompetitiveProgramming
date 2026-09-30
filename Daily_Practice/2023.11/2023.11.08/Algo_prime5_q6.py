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
    N = int(input())
    if N == 1:
        return 1 
    
    li = factorize(N)
    # print(li)

    diff = True

    for i in range(len(li)):
        num = li[i][1]
        if num > 1:
            diff = False 
    
    if diff:
        return (-1) ** len(li)
    else:
        return 0

print(main())
