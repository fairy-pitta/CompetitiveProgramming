# Q2: 部分和問題

def main():
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    # 0個からN個までカバーしたいので高さはN+1
    # 0からMまで重さをカバーしたいので幅はM+1
    field = [[(False) for _ in range(M+1)] for _ in range(N+1)]
    field[0][0] = True
    for row in range(N):
        for col in range(M+1):
            if field[row][col]:
                field[row+1][col] = True
                if col + W[row] <= M:
                    field[row+1][col+W[row]] = True
    
    return field[N][M]

if main():
    print("Yes")
else:
    print('No')



            


