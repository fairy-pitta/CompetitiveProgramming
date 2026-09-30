def main():
    X, Y = map(int,input().split())
    ans = 1
    num = X

    while True:

        num *= 2
        if num > Y:
            break
        ans += 1

    print(ans)

main()
