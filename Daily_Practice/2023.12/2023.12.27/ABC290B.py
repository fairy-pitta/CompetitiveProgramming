def main():
    N, K = map(int, input().split())
    S = input()

    finalist = 0
    ans = ""
    for i in range(len(S)):
        if S[i] == "o" and finalist < K:
            ans += "o"
            finalist += 1
        else:
            ans += "x"
    
    print(ans)

main()