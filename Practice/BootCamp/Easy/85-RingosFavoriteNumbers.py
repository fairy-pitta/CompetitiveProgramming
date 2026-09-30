def main():
    D, N = map(int, input().split())

    if D == 0:
        ans = 0
        cnt = 0
        while True:

            if cnt == N:
                break
            else:
                ans += 1
                if ans%100 != 0:
                    cnt += 1
        
        return ans 
    
    elif D == 1:
        if N == 100:
            return (N+1) * 100
        else:
            return N * 100
    
    else:
        if N == 100:
            return (N+1) * 100 *100
        else:
            return N * 100 * 100

print(main())
            