from itertools import combinations
from math import gcd
prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


N = int(input())
X = list(map(int, input().split()))
ans = []

for i in range(1, 16):
    comb_li = list(combinations(prime_list, i))
    for j in comb_li:
        num = 1
        for k in j:
            num *= k
        flag = True
        for item in X:
            if gcd(item, num) == 1:
                flag = False
        if flag:
            ans.append(num)
            break

print(min(ans))
