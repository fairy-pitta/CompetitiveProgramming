
def main():
    target = set(["A", "C", "G", "T"])
    ans = 0
    S = list(input())
    for i in range(len(S)):
        if S[i] in target:
            length = 0
            for j in range(i, len(S)):
                if S[j] in target:
                    length += 1
                else:
                    break
            ans = max(ans, length)

    
    print(ans)

main()
            