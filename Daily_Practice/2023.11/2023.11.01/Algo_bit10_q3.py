
def main():
    N, M = map(int, input().split())
    ans = 0
    W = list(map(int, input().split()))
    V = list(map(int, input().split()))

    for i in range(2**N):
        weight = 0
        value = 0
        for j in range(N):
            if i&(1<<j) > 0:
                weight += W[j]
                value += V[j]
        if weight <= M:
            ans = max(ans, value)
    
    print(ans)

main()            