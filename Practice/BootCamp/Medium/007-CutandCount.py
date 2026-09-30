def main():
    N = int(input())
    S = list(input())

    ans = 0
    for i in range(1, N-1):
        first_set = set(S[:i])
        second_set = set(S[i:])
        cnt = 0
        for item in first_set:
            if item in second_set:
                cnt += 1
        
        ans = max(cnt, ans)
    
    print(ans)

main()