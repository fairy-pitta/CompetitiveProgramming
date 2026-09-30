
def main():
    N = int(input())
    d = sorted(list(map(int, input().split())))

    left_bound = d[N//2-1]
    right_bound = d[N//2]

    print(right_bound-left_bound)

main()