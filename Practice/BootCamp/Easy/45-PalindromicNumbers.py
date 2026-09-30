def main():
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B+1):
        sentence = list(str(i))
        if sentence == sentence[::-1]:
            cnt += 1
    print(cnt)

main()

