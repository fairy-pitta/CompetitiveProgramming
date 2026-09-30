def main():
    H, W = map(int, input().split())
    G = []
    dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for _ in range(H):
        s = input()
        G.append(s)
    cnt = 0
    for row in range(1, H-1):
        for col in range(1, W-1):
            if G[row][col] != ".":
                continue 
            flag = True
            for r, c in dir:
                nr = row+r
                nc = col+c
                if G[nr][nc] != "#":
                    flag = False
            
            if flag:
                cnt += 1
    
    print(cnt)

main()
