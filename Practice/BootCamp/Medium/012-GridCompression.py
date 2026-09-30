def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    col_list = set()
    for col in range(W):
        flag = True
        for row in range(H):
            if A[row][col] == "#":
                flag = False 
        
        if flag:
            col_list.add(col)
    
    for r in range(H):
        if len(set(A[r])) == 1 and A[r][0] == ".":
            continue
        a = ""
        for c in range(W):
            if c not in col_list:
                a += A[r][c]
        print(a)

def solve():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    row_list = set()
    col_list = set()

    for row in range(H):
        for col in range(W):
            if A[row][col] == "#":
                row_list.add(row)
                col_list.add(col)
    
    for r in range(H):
        ans = ""
        for c in range(W):
            if r in row_list and c in col_list:
                ans += A[r][c]
        if ans == "":
            continue
        else:
            print(ans)

solve()