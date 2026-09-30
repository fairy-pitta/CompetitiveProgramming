def isint(): return int(input())
def ismap(): return map(int, input().split())
def islist(): return list(input())
def isgraph(N): return [[] for _ in range(N)]
def isdist(N, s): return [(s) for _ in range(N)]
def isseen(N): return [(False) for _ in range(N)]

MOD = 1000000007



def main():
    K = isint()
    # if K is not a multiple of 9
    if K % 9 != 0:
        # exit 
        return 0 
    # dp list 
    dp = isdist(K+1, 0)
    # why? 
    dp[0] = 1 
    # from dp[i-9] to dp[i-1]
    # if i is less than 9 
    # no need to care -> max 
    for i in range(1, K+1):
        dp[i] = sum(dp[max(0, i-9):i])
    
    return dp[-1] % MOD

print(main())
        

