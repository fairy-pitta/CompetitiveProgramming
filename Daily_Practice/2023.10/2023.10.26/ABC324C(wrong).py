
# let A be the string shared between T and T dash 
# let B be the string shared between T and T dash, but from the back 

def main():
    N, T = map(str, input().split())
    T = list(T)
    ans = []

    for i in range(int(N)):
        s = list(input())

        A = 0
        B = 0

        str_len = min(len(s), len(T))

        for j in range(str_len):
            if s[j] == T[j]:
                A += 1
            else: break 
        
        s_reversed = list(reversed(s))
        T_reversed = list(reversed(T))

        for k in range(str_len):
            if s_reversed[k] == T_reversed[k]:
                B += 1
            else: break 
        
        # print(A, B)
        # T'はTと等しい
        if s == T:
            ans.append(i+1)
        # TはT'のいずれか一つの位置に英小文字を一つ挿入して得られる文字列
        elif A + B + 1 == len(T) == len(s) + 1:
            ans.append(i+1)
        # T'はTからある一文字を削除して得られる文字列
        elif A + B == len(T) and len(s) - 1 == len(T):
            ans.append(i+1)
        # T'はTのある一文字を別の英小文字に変更して得られる文字列
        elif A + B + 1 == len(T) == len(s):
            ans.append(i+1)
        else: continue 
    
    print(len(ans))
    print(*ans)

    return 

main()