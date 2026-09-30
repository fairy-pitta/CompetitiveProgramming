
def main():
    Q, H, S, D = map(int, input().split())
    N = int(input())

    min_for_two_litters = min(Q*8, H*4, S*2, D)
    min_for_one_litters = min(Q*4, H*2, S)

    if N%2:
        print(N//2*min_for_two_litters+min_for_one_litters)
    else:
        print(N//2*min_for_two_litters)
    
    return


main()