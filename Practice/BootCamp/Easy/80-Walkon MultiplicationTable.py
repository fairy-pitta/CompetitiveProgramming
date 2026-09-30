def calc_divisors(N) -> list:
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
    li = calc_divisors(N)

    ans = 10**18

    for i in li:
        up = N // i
        ans = min(ans, up+i-2)
    
    print(ans)

main()
