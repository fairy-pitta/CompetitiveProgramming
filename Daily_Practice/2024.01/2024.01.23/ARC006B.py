
N, L = map(int, input().split())
G = [input() for _ in range(L)]
y = input()  # ゴールの位置

goal = y.index("o")

# 各開始位置からの経路を計算
for pos in range(N):
    cur = pos * 2
    for i in range(L):
        if cur > 0 and G[i][cur-1] == "-":
            cur -= 2
        elif cur < N * 2 - 2 and G[i][cur+1] == "-":
            cur += 2

    if cur == goal:
        print(pos+1)
        break

