
def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    Q = [0]
    for i in range(N):
        Q.append(Q[i]+P[i])

    s = 0
    for i in range(1, N-K+2):
        temp = Q[i+K-1] - Q[i-1]
        s = max(s, temp)

    
    print((s+K) / 2)
    
main()
