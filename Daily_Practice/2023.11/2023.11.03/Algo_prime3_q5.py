def calc_divisors(N, b):
    res = []

    for i in range(1, N+1):
        if i * i > N:
            break 

        if N % i != 0:
            continue 

        if i > b:
            res.append(i)

        if N // i != i and N // i > b:
            res.append(N // i)
    
    res.sort()

    return res 


# 

def main():
    A, B = map(int, input().split())
    n = A - B
    li = calc_divisors(n, B)
    print(li)
    



def just_do_it(A, B):
    li = []
    for i in range(1, A):
        if A % i == B:
            li.append(i)
    
    return li



# 411522611, 1234567833