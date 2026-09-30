import math

# https://note.nkmk.me/python-gcd-lcm/
def my_lcm(x: int, y: int) -> int:
    return (x * y) // math.gcd(x, y)



def calculate_gcd_of_int_list(A: list) -> int:
    import math
    if len(A) == 1:
        return A[0]
    gcd = A[0]
    for i in range(len(A)):
        gcd = math.gcd(gcd, A[i])

    return gcd


def factorize(N: int) -> list:
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
    A = list(map(int, input().split()))
    gcd = calculate_gcd_of_int_list(A)
    li = factorize(gcd)
    ans = 1
    for i in range(len(li)):
        num = li[i][1]
        ans *= num + 1
    return ans 

print(main())