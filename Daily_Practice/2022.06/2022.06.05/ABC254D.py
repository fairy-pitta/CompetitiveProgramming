# together sum 

from itertools import count 

def calc_odd_factor_prod(n):
    # 次数が奇数の素因数の積を得る
    for sq_i in (i * i for i in count(2)):
        # 無限イテレータ (2,3,4,5,6...)
        # 第一引数startでスタートを指定する
        # 第二引数stepで増減を指定可能

        if sq_i > n:
            break 
        while n % sq_i == 0:
            # 平方数で割ってその商を置き換える
            n = n //sq_i # n //= sq_i
    return n

def main():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        odd = calc_odd_factor_prod(i)
        for j in range(1, N+1):
            if odd * j * j > N:
                break 
            ans += 1
    return ans 

print(main())