

def main():
    N, T = map(str, input().split())
    N = int(N)
    T = list(T)

    ans = []

    for i in range(N):
        flag = False
        s = list(input())

        if len(s) == len(T):
            wrong = 0
            for j in range(len(s)):
                if s[j] != T[j]:
                    wrong += 1
            
            if wrong <= 1:
                ans.append(i+1)
        
        elif abs(len(s)-len(T)) == 1:
            long, short = s, T
            if len(s) < len(T):
                long, short = T, s
            
            
            for j in range(len(short)):
                if short[j] != long[j] and short[j:] == long[j+1:]:
                        flag = True
                        break
                elif short[j] != long[j] and short[j:] != long[j+1:]:
                    flag = False
                    break

                flag = True
        else:
            flag = False
        
        if flag:
            ans.append(i+1)

    print(len(ans))
    print(*ans)

main()






