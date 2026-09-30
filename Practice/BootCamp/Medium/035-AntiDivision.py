import math 
def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)

def main():
    A, B, C, D = map(int, input().split())
    cd = my_lcm(C, D)
    less_A = A-1

    a_num = (less_A//C) + (less_A//D) - (less_A//cd)
    b_num = (B//C) + (B//D) - (B//cd)

    
    print(B-A+1-b_num+a_num)

main()


