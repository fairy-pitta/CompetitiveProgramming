H, W = map(int, input().split())
field = []
for _ in range(H):
    s = list(input())
    field.append(s)

print(field)
result = [[0 for c in range(W)] for r in range(H)]

for row in range(H):
    for column in range(W):
        if field[row][column] == ".":
            # upper 
            if row >= 1:
                # up
                if field[row-1][column] == "#": result[row][column] += 1
                else: continue


                # upperleft 
                if column >= 1: 
                    if field[row-1][column-1] == "#": result[row][column] += 1
                    else: continue 
                else: continue 

                # upperright 
                if column < (W-1):
                    if field[row-1][column+1]: result[row][column] += 1
                    else: continue
            print(result)

            # horizontal 
            # left 
            if column >= 1: 
                if field[row][column-1] == "#": result[row][column] += 1
                else: continue
            # right 
            if column < (W-1):
                if field[row][column+1] == "#": result[row][column] += 1
                else: continue 
            
            print(result)
            
            # lower
            if row < (H-1):
                # down
                if field[row+1][column] == "#": result[row][column] += 1
                else: continue 

                # lower left 
                if column >= 1:
                    if field[row+1][column-1] == "#": result[row][column] += 1
                    else: continue 
                # lower right 
                if column <= (W-1): 
                    if field[row+1][column+1] == "#": result[row][column] += 1
                    else: continue 
        else: 
            result[row][column] = "#" 

for i in range(H):
    ans = "".join([str(_) for _ in result[i]])
    print(ans)
            

                


