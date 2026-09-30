

def main():
    N, K = map(int, input().split())
    ans = 0
    MOD = 10**9+7
    li = [i for i in range(N+1)]
    L = [0]
    R = [0]

    for j in range(len(li)):
        L.append(L[-1] + li[j])
        R.append(R[-1] + li[-j-1])
    
    # print(L)
    # print(R)
    for k in range(K, N+2):
        small = L[k]
        large = R[k]
        ans += (large-small+1)%MOD
    
    print(ans%MOD)

main()
