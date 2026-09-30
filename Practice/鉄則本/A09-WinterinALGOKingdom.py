def accumulative_sum_2d(g):
    nrow = len(g)
    ncol = len(g[0])
    A = [[(0) for _ in range(ncol)] for _ in range(nrow)]
    for r in range(nrow):
        for c in range(ncol):
            if c == 0:
                A[r][c] = g[r][c]
            else:
                A[r][c] = g[r][c] + A[r][c-1]

    for c in range(ncol):
        for r in range(1, nrow):
            A[r][c] = A[r][c] + A[r-1][c]
    
    return A

def main():
    H, W, N = map(int, input().split())
    G = [[(0) for _ in range(W)] for _ in range(H)]
    for _ in range(N):
        a, b, c, d = map(int, input().split())
        a -= 1
        b -= 1
        c -= 1
        d -= 1 
        G[a][b] += 1
        # top right
        if d<W-1: G[a][d+1] -= 1
        # bottom left 
        if c<H-1: G[c+1][b] -= 1
        # bottom right 
        if d<W-1 and c<H-1: G[c+1][d+1] += 1

    ans = accumulative_sum_2d(G)
    for row in range(len(G)):
        print(*ans[row])

main()



        