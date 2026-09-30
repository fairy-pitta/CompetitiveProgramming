from bisect import insort_left, bisect_left, bisect_right
Q = int(input())
stack = []
for quary in range(Q):
    new = list(map(int, input().split()))
    if new[0] == 1:
        x = int(new[1])
        insort_left(stack, x)
    elif new[0] == 2:
        num = stack.count(new[1])
        num = min(num, new[2])
        for _ in range(num):
            stack.remove(new[1])
    else:
        maximum = stack[-1]
        print(maximum - stack[0])
            



