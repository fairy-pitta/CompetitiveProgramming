def main():
    S = list(input())
    K = int(input())

    one_num = 0
    for i in range(len(S)):
        if S[i] == "1":
            one_num += 1
        else:
            break

    if K <= one_num:
        print(1)
    else:
        print(S[one_num])

main()