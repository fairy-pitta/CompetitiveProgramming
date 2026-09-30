def main():
    N = int(input())
    A = list(map(int, input().split()))

    top_coder = 0
    color_set = set()

    for i in range(N):
        if A[i] < 400:
            color_set.add("grey")
        elif A[i] < 800:
            color_set.add("brown")
        elif A[i] < 1200:
            color_set.add("green")
        elif A[i] < 1600:
            color_set.add("skyblue")
        elif A[i] < 2000:
            color_set.add("blue")
        elif A[i] < 2400:
            color_set.add("yellow")
        elif A[i] < 2800:
            color_set.add("orange")
        elif A[i] < 3200:
            color_set.add("red")
        else:
            top_coder += 1 
    
    max_num = len(color_set) + top_coder
    min_num = 1 if len(color_set) == 0 else len(color_set)

    print(min_num, max_num)

main()