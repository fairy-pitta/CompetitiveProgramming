def main():
    N, A, B = map(int, input().split())
    upper_A = (N // A) * A
    upper_B = (N // B) * B
    #print(upper_A, upper_B)
    from math import gcd 
    from decimal import Decimal
    lcm = (A * B) // gcd(A, B)
    upper_AB = (N // lcm) * lcm

    sum_A = (A + upper_A) * (N // A) 
    sum_B = (B + upper_B) * (N // B) 
    sum_AB = (lcm + upper_AB) * (N // lcm) 
    sum_all = (1 + N) * N 


    ans = (sum_all - sum_A - sum_B + sum_AB) // 2
    return "{0:.0f}".format(Decimal(ans))
print(main())

