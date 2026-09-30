
def main():
    N, A, B = map(int, input().split())

    # check A < B
    if A > B:
        print(0)
        return 
    
    min_sum = (N-1)*A+B
    max_sum = (N-1)*B+A
    print(max_sum-min_sum+1 if (max_sum-min_sum) >= 0 else 0)
    return

main()