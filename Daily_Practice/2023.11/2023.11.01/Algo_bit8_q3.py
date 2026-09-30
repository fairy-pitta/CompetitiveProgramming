def main():
    X = list(map(int, input().split()))

    for i in range(len(X)):
        row = ""
        for digit in range(8):
            if (X[i] & (1<<(digit*2)) == 0 and \
                X[i] & (1<<(digit*2+1)) == 0):
                row += "."
            elif (X[i] & ((1<<digit*2)) == 0 and \
                X[i] & ((1<<digit*2+1)) > 0):
                row += "x"
            else:
                row += "o"
        print(row[::-1])

main()
