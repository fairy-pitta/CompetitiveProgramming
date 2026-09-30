
def main():
    H, W = map(int, input().split())
    A = list(map(int, input().split()))
    field = [[(False) for _ in range(W)] for _ in range(H)]
    field[0][0] = True
    for row in range(H-1):
        for col in range(W):
            if field[row][col]:
                field[row+1][col] = True
                if col + A[row] <= W-1:
                    field[row+1][col+A[row]] = True
    
    # print(field)
    return sum(field[-1])

print(main())


