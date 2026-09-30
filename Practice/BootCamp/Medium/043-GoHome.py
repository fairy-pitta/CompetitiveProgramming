
def main():
    X = abs(int(input()))
    i = 0

    while True:
        if (0+i) * (i-0+1) // 2 >= X:
            break 
        i += 1
    
    print(i)

main()

