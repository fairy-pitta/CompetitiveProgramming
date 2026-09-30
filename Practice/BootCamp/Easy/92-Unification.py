def main():
    S = list(input())

    one = S.count("1")
    zero = S.count("0")

    print(min(one, zero)*2)

main()
