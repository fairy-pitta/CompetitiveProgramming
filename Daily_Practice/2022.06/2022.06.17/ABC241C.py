def main():
    N = int(input())
    pat = [(1,0), (0, 1), (1,-1), (1,1)]
    
    # convert field to the numbers

        # where to move (row, col)
        # # down, right, down+left, down+right 
    field = [[1 if i == "#" else 0 for i in input()] for _ in range(N)]
   
    # judge, when taken 6,
    # # if there are more than or equal to 4 blacks 
    
    def judge(start_row, start_col, go_row, go_col, N, field):
        black = 0
        for _ in range(6):
            if not (0 <= start_row < N and 0 <= start_col < N):
                return False 
            black += field[start_row][start_col]
            start_row += go_row
            start_col += go_col
        return black >= 4
    
    for row in range(N):
        for col in range(N):
            for go_row, go_col in pat:
                if judge(row, col, go_row, go_col, N, field):
                    return True
        
    
    return False

print("Yes" if main() else "No")



                        