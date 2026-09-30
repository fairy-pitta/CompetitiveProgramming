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

def factor_numbers(N):
    li = factorize(N)
    ans = 1
    for i in range(len(li)):
        num = li[i][1] + 1 
        ans *= num
    return ans 


def main():
    ans_num = 0
    ans = []
    n = 1
    while ans_num < 5:
        if factor_numbers(n) == 6:
            ans.append(n)
            ans_num += 1
        n += 1

    print(*ans)
    return

main()
            
        
