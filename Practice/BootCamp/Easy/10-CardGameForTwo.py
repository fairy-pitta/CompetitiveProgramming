
def main():
    N = int(input())
    A = sorted(list(map(int, input().split())), reverse=True)
    Alice = 0
    Bob = 0
    
    for i in range(N):
        if not i%2: 
            Alice += A[i]
        else:
            Bob += A[i]
    
    print(Alice-Bob)

main()