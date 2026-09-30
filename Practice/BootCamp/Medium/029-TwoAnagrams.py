
def main():
    s = "".join(sorted(list(input())))
    t = "".join(sorted(list(input()), reverse=True))

    if s < t:
        print("Yes")
    else:
        print("No")


main()