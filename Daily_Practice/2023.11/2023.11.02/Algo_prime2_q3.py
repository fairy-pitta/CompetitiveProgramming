# judge if i is prime for all integer i between 1 and N
def Eratosthenes(N):
    isprime = [True] * (N+1)
    # 0 and 1 are not prime numbers 
    isprime[0], isprime[1] = False, False

    for p in range(2, N+1):
        # if its already a composite number, skip
        if not isprime[p]: continue

        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p
        
    return isprime 


def main():
    N = int(input())
    li = Eratosthenes(N)
    print(sum(li))

main()


