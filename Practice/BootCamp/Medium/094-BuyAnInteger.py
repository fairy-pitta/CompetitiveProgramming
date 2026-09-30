def main():
    A, B, X = map(int, input().split())
    
    if 10**9*A + B*10 < X:
        ans = 10**9
    else:
        ans = 0

    for digit in reversed(range(1, 10)):
        BdN = B * digit 
        AN = X - BdN
        if AN > 0:
            max_N = AN // A
            # print(max_N)
            if len(list(str(max_N))) > digit:
                max_N = int("9"*digit)
            if max_N <= 10**9 and max_N*A + BdN <= X:
                ans = max(ans, max_N)
    print(ans)

main()