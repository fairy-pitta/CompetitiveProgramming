def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = int(input())
        S.append(s)

    S_sum = sum(S)

    non_zero = []
    for i in S:
        if i % 10 != 0:
            non_zero.append(i)
    
    if S_sum % 10 != 0:
        print(S_sum)
    else:
        if len(non_zero) > 0:
            S_sum -= min(non_zero)
            print(S_sum)
        else:
            print(0)

main()
