def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = list(input())

    ans = 0
    hand_li = []
    for i in range(N):
        if i < K:
            if T[i] == "r":
                hand_li.append("p")
                ans += P
            elif T[i] == "p":
                hand_li.append("s")
                ans += S
            else:
                hand_li.append("r")
                ans += R
        else:
            if T[i] == "r" and hand_li[i-K] != "p":
                hand_li.append("p")
                ans += P
            elif T[i] == "p" and hand_li[i-K] != "s":
                hand_li.append("s")
                ans += S
            elif T[i] == "s" and hand_li[i-K] != "r":
                hand_li.append("r")
                ans += R   
            else:
                hand_li.append("f")
    
    print(ans)

main()