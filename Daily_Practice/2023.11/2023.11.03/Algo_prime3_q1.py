def calc_divisors(N):
    res = []

    for i in range(1, N+1):
        if i * i > N:
            break 

        if N % i != 0:
            continue 

        res.append(i)

        if N // i != i:
            res.append(N // i)
    
    res.sort()

    return res 

def main():
    N = int(input())
    divisors_list = calc_divisors(N)
    if sum(divisors_list) == N * 2:
        print("Yes")
    else:
        print("No")

main()