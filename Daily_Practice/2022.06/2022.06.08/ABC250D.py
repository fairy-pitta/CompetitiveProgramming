# def eratosthenes2(n):
#     is_prime = ([False, True] * (n//2+1))[0: n+1]
#     is_prime[1] = False
#     is_prime[2] = True
#     for i in range(3, n+1, 2):
#         if not(is_prime[i]):
#             continue
#         if i*i > n:
#             break
#         for k in range(i*i, n+1, i):
#             is_prime[k] = False
#     return is_prime


# def main():
#     N = int(input())
#     max_q = int(N ** (1/3))
#     primes = eratosthenes2(N) if N >= 2 else [False * N]
#     ans = 0
#     for prime in range(max_q):
#         if not primes[prime]:
#             continue 
#         else:
#             q = prime ** 3
#             max_p = N // q
#             # print(max_p, "max_p", q, "q")
#             for candidate in range(max_p+1):
#                 if not primes[candidate]:
#                     continue 
#                 else:
#                     if prime <= candidate:
#                         break
#                     else:
#                         if candidate * q > N:
#                             break 
#                         else:
#                             # print(candidate * q)
#                             ans += 1
#     return ans 

# print(main())


def primes_list(n):
    prime_flag = [1] * (n + 1)
    prime_flag[0] = 0
    prime_flag[1] = 0

    i = 2
    while i * i <= n:
        if prime_flag[i]:
            for j in range(2 * i, n + 1, i):
                prime_flag[j] = 0
        i += 1
    return [i for i in range(n + 1) if prime_flag[i]]

def main():
    N = int(input())
    max_q = int(N ** (1/3))
    ans = 0
    primes = primes_list(max_q)
    for prime in range(len(primes)):
        q = primes[prime] ** 3 
        for candidate in range(prime):
            p = primes[candidate]
            if p * q > N:
                break 
            ans += 1 
    return ans 

print(main())