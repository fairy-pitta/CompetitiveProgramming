prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


def divisors(N):
    li = []
    for i in prime_list:
        if N % i == 0:
            li.append(i)
            while N % i == 0:
                N //= i
    return li


s = set()

N = int(input())
X = list(map(int, input().split()))

for item in X:
    prime_factors = divisors(item)
    s.add(prime_factors[0])


ans_li = list(s)
ans = 1

for num in ans_li:
    ans *= num

print(ans)
