def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == "U":
            # going up
            ans += len(S)-(i+1)
            # going down
            ans += 2 * i
        else:
            # going up
            ans += 2 * (len(S)-(i+1))
            ans += i
    
    print(ans)

main()