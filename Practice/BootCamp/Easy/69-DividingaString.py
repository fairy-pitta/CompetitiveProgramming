


def main():
    S = input()

    cnt = 0
    curr = ""
    prev = ""

    for i in range(len(S)):
        curr += S[i]
        if prev != curr:
            cnt += 1
            prev = curr
            curr = ""
    print(cnt)

main()

        



