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
    ans = []
    li = factorize(N)
    print(li)
    for i in range(len(li)):
        factor, time = li[i][0], li[i][1]
        for _ in range(time):
            ans.append(factor)
    
    print(ans)

main()