
def main():
    N, A, B = map(int, input().split())
    S = list(input())

    confirmed = 0
    foreign_rank = 0

    for participant in S:
        if participant == "a":
            if confirmed < A+B:
                print("Yes")
                confirmed += 1
            else:
                print("No")
        elif participant == "b":
            if confirmed < A+B and foreign_rank < B:
                print("Yes")
                confirmed += 1
                foreign_rank += 1
            else:
                print("No")
                foreign_rank += 1 
        else:
            print("No")
    
    return 

main()