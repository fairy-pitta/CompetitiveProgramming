from re import L


def main():
    H, W = map(int, input().split())
    field = []
    row_sum = []
    col_sum = [(0) for _ in range(W)]
    for i in range(H):
        a = list(map(int, input().split()))
        field.append(a)
        row_sum.append(sum(a))
    for j in range(W):
        for l in range(H):
            col_sum[j] += field[l][j]
    # print(field, col_sum, row_sum)
    ans = [[(0) for _ in range(W)] for _ in range(H)]
    for row in range(H):
        for col in range(W):
            # print(row_sum[row], col_sum[col], field[row][col])
            ans[row][col] = row_sum[row] + col_sum[col] - field[row][col]
    
    for k in range(H):
        print(*ans[k])

main()