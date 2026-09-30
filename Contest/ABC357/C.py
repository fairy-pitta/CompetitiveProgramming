N = int(input())



def draw(N):
    length = 3 ** N

    def block(grid, top, left, size):
        if size == 1:
            grid[top][left] = "#"
            return 
        
        nex_size = size // 3

        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    for k in range(nex_size):
                        for l in range(nex_size):
                            grid[top + i * nex_size + k][left + j * nex_size + l] = '.'
                else:
                    block(grid, top + i * nex_size, left + j * nex_size, nex_size)

    grid = [['#' for _ in range(3**N)] for _ in range(3**N)]
    block(grid, 0, 0, length)

    return grid

ans = draw(N)
for r in ans:
    print("".join(r))