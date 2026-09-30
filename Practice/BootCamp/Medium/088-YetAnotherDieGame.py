
def main():
    x = int(input())

    num = x // 11 * 2
    res = x % 11
    if res > 6:
        num += 2
    elif res == 0:
        num = num
    else:
        num += 1
    
    print(num)

main()