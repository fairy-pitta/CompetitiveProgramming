from bisect import bisect_right, bisect_left

def main():
    N = int(input())
    A = list(map(int, input().split()))

    
    # pos = []
    # for i in range(N+1):
    #     pos.append([indx for indx, x in enumerate(A) if x == i])
    
    pos = [[] for _ in range(N+1)]
    for i, x in enumerate(A, 1):
        pos[x].append(i)
    
    # print(pos)

    Q = int(input())
    for q in range(Q):
        l, r, x = map(int, input().split())
        left = bisect_left(pos[x], l)
        right = bisect_right(pos[x], r)
        # print(left, right)
        print(right - left)

main()
    