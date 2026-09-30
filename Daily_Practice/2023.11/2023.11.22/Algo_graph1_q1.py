
def main():
    N, A, B = map(int, input().split())
    G = []
    for _ in range(N):
        s = list(input())
        G.append(s)
    
    # print(G)

    if G[A][B] == "o":
        print("Yes")
    else:
        print("No")

main()
