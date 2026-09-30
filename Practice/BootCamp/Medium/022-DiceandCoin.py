
def main():
    N, K = map(int, input().split())

    prob = 0

    for i in range(1, N+1):

        cnt = 0
        n = i
        while True:
            if n < K:
                n *= 2 
                cnt += 1
            else:
                break 
        
        prob += (1/N) * (1/2) ** cnt
    
    print(prob)

main()
