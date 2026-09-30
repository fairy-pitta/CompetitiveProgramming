def main():
    a, b = map(int, input().split())
    if a <= 0 <= b:
        print("Zero")
    elif a < 0:
        cnt = 0
        if b > 0:
            cnt = abs(a)
        else:
            cnt = abs(a-b)+1
        if cnt%2:
            print("Negative")
        else:
            print("Positive")
    else:
        print("Positive")

main()