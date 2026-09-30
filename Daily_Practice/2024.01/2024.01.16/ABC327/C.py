A = [list(map(int, input().split())) for _ in range(9)]
li = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def split_and_flatten_subgrids(grid):
    flattened_subgrids = []
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            subgrid = [grid[r][c] for r in range(row, row+3) for c in range(col, col+3)]
            flattened_subgrids.append(subgrid)
    return flattened_subgrids

flag = True

for r in range(9):
    if sorted(A[r]) != li:
        flag = False 


for c in range(9):
    tmp = []
    for r in range(9):
        tmp.append(A[r][c])
    if sorted(tmp) != li:
        flag = False


new_A = split_and_flatten_subgrids(A)

for grid in new_A:
    if sorted(grid) != li:
        flag = False

if flag:
    print("Yes")
else:
    print("No")
