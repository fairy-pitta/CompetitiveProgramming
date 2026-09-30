def main():
    N, Q = map(int, input().split())
    S = input()
    li = []
    for i in range(N):
        if i == 0:
            li.append(0)
        else:
            if S[i-1] == "A" and S[i] == "C":
                li.append(li[-1]+1)
            else:
                li.append(li[-1])
    
    for _ in range(Q):
        l, r = map(int, input().split())
        print(li[r-1]-li[l-1])

main()

