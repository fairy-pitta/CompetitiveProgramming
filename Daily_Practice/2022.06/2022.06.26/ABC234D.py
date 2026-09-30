from collections import deque
def main():
    H, W = map(int, input().split())
    field = []
    for row in range(H):
        c = list(input())
        field.append(c)

    stack = deque()
    dp = [[(0) for _ in range(W)] for _ in range(H)]

    # print(field)
    # print(dp)

    dp[0][0] = 1
    m = 1
    s = set()
    stack.append((0,0))
    s.add((0,0))
    direction = [(0,1), (1,0)]
    while len(stack) > 0:
        y,x = stack.popleft()
        for d in direction:
            i,j = d
            # print(dp)
            togo_y = y + i
            togo_x = x + j
            if togo_y < H and togo_x < W:
                if field[togo_y][togo_x] == ".":
                    dp[togo_y][togo_x] = max(dp[y][x] + 1, dp[togo_y][togo_x])
                    m = max(m, dp[togo_y][togo_x])
                    if (togo_y, togo_x) not in s:
                        stack.append((togo_y, togo_x))
                        s.add((togo_y, togo_x))
                    else:
                        continue
                else:
                    continue
            else:
                continue
    return m 

print(main())
