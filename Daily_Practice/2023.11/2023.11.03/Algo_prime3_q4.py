def divisors_sum(N):
    res = []

    for i in range(1, N+1):
        if i * i > N:
            break 

        if N % i != 0:
            continue 

        res.append(N//i + i)
    

    return min(res) 

def main():
    N = int(input())
    print(divisors_sum(N))

main()

