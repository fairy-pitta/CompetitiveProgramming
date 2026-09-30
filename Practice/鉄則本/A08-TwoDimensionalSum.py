def main():
    H, W = map(int, input().split())
    Grid = []
    for _ in range(H):
        li = list(map(int, input().split()))
        x = [li[0]]
        for i in range(1, W):
            x.append(x[-1]+li[i])
        Grid.append(x)
    
    for c in range(W):
        for r in range(1, H):
            Grid[r][c] += Grid[r-1][c]
    

    Q = int(input())
    for _ in range(Q):
        a, b, c, d = map(int, input().split())
        a -= 1
        b -= 1
        c -= 1
        d -= 1
        top_left = Grid[a-1][b-1] if a>0 and b>0 else 0
        bottom_left = Grid[c][b-1] if b>0 else 0
        top_right = Grid[a-1][d] if a>0 else 0
        bottom_right = Grid[c][d]
        print(bottom_right-top_right-bottom_left+top_left)
    





main()
    