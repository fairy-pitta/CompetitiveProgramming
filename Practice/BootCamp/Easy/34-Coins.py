def main():
    A = int(input())
    B = int(input())
    C = int(input())
    X = int(input())

    cnt = 0

    for five_hundred in range(A+1):
        for hundred in range(B+1):
            for fifty in range(C+1):
                if five_hundred*500+hundred*100+fifty*50==X:
                    cnt += 1
    
    print(cnt)

main()