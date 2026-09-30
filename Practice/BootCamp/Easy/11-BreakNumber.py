from bisect import bisect_right 

multiple_of_two = [2**i for i in range(8)]

def main():
    N = int(input())
    idx = bisect_right(multiple_of_two, N)
    print(multiple_of_two[idx-1])

main()
