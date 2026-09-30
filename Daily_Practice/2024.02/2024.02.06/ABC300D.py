N = int(input())

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

li = primes_list(int(N**0.5)+1)

ans = 0
for i in range(len(li)):
    for j in range(i+1, len(li)):
        for k in range(j+1, len(li)):
            if i ** 2 * j * k ** 2 <= N:
                ans += 1

print(ans)