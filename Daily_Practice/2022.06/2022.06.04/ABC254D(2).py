# https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


from bisect import bisect_right

def main():
    N = int(input())
    ans = 0
    for original in range(1, N+1):
        sqn = original ** 2
        di = make_divisors(sqn)
        index = bisect_right(di, N)
        x = index * 2 - len(di)
        ans += (x // 2) * 2
        ans += 1
    return ans 
print(main())
