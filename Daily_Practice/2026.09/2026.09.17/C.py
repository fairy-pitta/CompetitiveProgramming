def main():
    S = input()
    K = int(input())

    ans = 0
    dots = 0  
    l = 0
    for r in range(len(S)):
        if S[r] == ".":
            dots += 1
        # '.' が K を超えたら、超えなくなるまで左端を縮める
        while dots > K:
            if S[l] == ".":
                dots -= 1
            l += 1
        ans = max(ans, r - l + 1)

    return ans


print(main())
