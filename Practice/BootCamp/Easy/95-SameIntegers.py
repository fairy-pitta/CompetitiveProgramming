def main():
    li = sorted(list(map(int, input().split())))
    cnt = li[2] - li[1]
    li[0] = li[0] + li[2] - li[1]
    diff = li[2] - li[0]
    cnt += diff // 2
    diff %= 2
    if diff == 1:
        cnt += 2
    
    print(cnt)

main()