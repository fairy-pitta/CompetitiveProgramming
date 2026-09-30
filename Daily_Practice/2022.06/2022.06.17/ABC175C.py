def main():
    X, K, D = map(int, input().split())
    dist = X 
    times = X // D
    if K - times < 0:
        print(X - (times * D))
    else:
        if (times - K) % 2 == 0:
            print(X % D)
        else:
            print(abs((X % D) - D))

main()