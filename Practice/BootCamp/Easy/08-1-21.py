def main():
    a, b = map(str, input().split())
    num = int(a+b)
    if (num**0.5//1)**2 == num:
        print("Yes")
    else:
        print("No")

main()
    