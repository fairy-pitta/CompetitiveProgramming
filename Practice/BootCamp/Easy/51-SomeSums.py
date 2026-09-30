def main():
    N, A, B = map(int, input().split())
    ans = 0
    for i in range(1, N+1):
        str_num = str(i)
        str_num_sum = sum([int(z) for z in list(str_num)])
        if A <= str_num_sum <= B:
            ans += i
    
    print(ans)

main()
