
dir = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]
    grids = [[(0) for _ in range(W)] for _ in range(H)]


    for row in range(H):
        for col in range(W):
            if S[row][col] == "#":
                grids[row][col] = "#"
            
                for r, c in dir:
                    adj_row = row+r
                    adj_col = col+c
                    if (0 <= adj_row < H and \
                        0 <= adj_col < W and \
                            S[adj_row][adj_col] == "."):
                        
                        grids[adj_row][adj_col] += 1
    
    for i in grids:
        ans = "".join([str(z) for z in i])
        print(ans)


main()



                    
                    

