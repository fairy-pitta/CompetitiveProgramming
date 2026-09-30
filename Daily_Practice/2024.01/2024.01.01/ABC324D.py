

def solve():
    N = int(input())
    S = list(input())
    S = sorted(S, reverse=True)
    max_num = int("".join(S))
    square_list = set()
    i = 0

    while True:
        square = i ** 2
        if square > max_num:
            break
        square_list.add(square)
        i += 1
    

    cnt = 0
    for square in square_list:
        num = str(square).zfill(N)
        flag = True
        for digit in range(10):
            d = str(digit)
            if num.count(d) != S.count(d):
                flag = False
                break

        if flag:
            cnt += 1

    print(cnt)

solve()



