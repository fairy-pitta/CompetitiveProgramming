
def main():
    H = int(input())
    cnt = 0
    num = 1
    while True:
        if H==1:
            cnt += 1
            break 
        H //= 2
        num *= 2
        cnt += num
    print(cnt)

main()


