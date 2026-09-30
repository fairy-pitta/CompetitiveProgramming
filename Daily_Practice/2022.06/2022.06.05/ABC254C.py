def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    
    # bubble sort 
    B = [[] for _ in range(K)] # 余りごとに管理するための二次元配列
    for index, element in enumerate(A):
        B[index % K].append(element)
    
    for i in range(K):
        B[i].sort() 
        # for each list in B, sort 
    
    SA = [0] * N
    for i in range(N):
        # merge bubbles 
        # when i = 0, B[0][0]
        # when i = 1, B[1][0]
        # when i = 2, B[2][0]
        # when i = 3, B[1][1]
        SA[i] = B[i % K][i // K]
    
    # check if restored version is the same as 
    # the ideally sorted version of A 
    return SA == sorted(A)

print("Yes" if main() else "No")

