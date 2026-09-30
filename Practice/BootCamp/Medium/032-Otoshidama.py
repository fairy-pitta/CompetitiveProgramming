
def main():
    N,Y = map(int, input().split())

    for i in range(N+1):
        for j in range(N+1):
            if N-i-j >= 0 and 10000*i+5000*j+1000*(N-i-j) == Y:
                print(i, j, N-i-j)
                return 
    
    print(-1, -1, -1)
    return 

main()