def main():
    K, A, B = map(int, input().split())

    if A >= B-2:
        print(K+1)
    else:
        if K + 1 >= A:
            print(((K-A+1)//2) * (B-A) + (A+(K-A+1-(K-A+1)//2*2) if (K-A+1)%2 != 0 else A))
        else:
            print(K+1)
            

main()
    

