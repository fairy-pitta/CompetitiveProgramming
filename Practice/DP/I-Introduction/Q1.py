
def main():
    N, X, Y = map(int, input().split())
    a = [X, Y]
    for i in range(2, N):
        a.append((a[i-1] + a[i-2]) % 100)
    
    print(a[N-1])
    return 

main()