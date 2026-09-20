def compress(A: list) -> list:
    A_sorted = sorted(set(A))
    sorted_idx = {x:i+1 for i,x in enumerate(A_sorted)}
    compressed_order = []
    for a in A:
        compressed_order.append(sorted_idx[a])
    return compressed_order

def main():
    H, W, N = map(int, input().split())
    row = []
    col = []
    for _ in range(N):
        r, c = map(int, input().split())
        row.append(r)
        col.append(c)

    compressed_rows = compress(row)
    compressed_cols = compress(col)

    for i in range(N):
        print(compressed_rows[i], compressed_cols[i])

main()

