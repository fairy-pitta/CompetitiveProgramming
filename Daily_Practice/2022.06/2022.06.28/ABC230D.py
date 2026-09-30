def main():
    N, A, B = map(int, input().split())
    A_B = A - B
    AB = A + B
    P, Q, R, S = map(int, input().split())
    Width = S - R + 1
    Height = Q - P + 1 
    for i in range(P, Q+1):
        ans = []
        for j in range(R, S+1):
            if i + j == AB or i - j == A_B:
                ans.append("#")
            else:
                ans.append(".")
        print(*ans, sep = "")



main()
