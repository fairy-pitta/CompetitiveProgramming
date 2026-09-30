
def islist(): return list(input())


# 定数ちゃん
# MOD = 998244353
# MOD = 1000000007
# INF = 10 ** 18 + 1

def main():
    S = islist()
    T = islist()
    name = set(list("atcoder"))
    ans = True
    for i in range(len(S)):
        if S[i] == T[i]:
            continue 
        elif S[i] == "@" and T[i] in name:
            continue 
        elif T[i] == "@" and S[i] in name:
            continue 
        ans = False
    
    if ans:
        print("You can win")
    else:
        print("You will lose")

main()