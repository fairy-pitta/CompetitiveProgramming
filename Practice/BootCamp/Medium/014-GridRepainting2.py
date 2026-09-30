def main():
    dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    for row in range(H):
        for col in range(W):
            if S[row][col] == "#":
                flag = False
                for r, c in dir:
                    adj_r = row + r
                    adj_c = col + c
                    if (0 <= adj_r < H and\
                        0 <= adj_c < W and\
                            S[adj_r][adj_c] == "#"):
                        flag = True
                
                if not flag: return flag 
                        
    
    return True

if main():
    print("Yes")
else:
    print("No")

