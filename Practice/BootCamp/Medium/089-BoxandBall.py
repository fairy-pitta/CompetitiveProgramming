def main():
    N, M = map(int, input().split())
    can_red = [(False) for _ in range(N)]
    num_ball = [(1) for _ in range(N)]
    can_red[0] = True


    for _ in range(M):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        if can_red[x]:
            # if there is a red ball in the box
            if num_ball[x] == 1:
                can_red[x] = False
                can_red[y] = True
                num_ball[x] -= 1
                num_ball[y] += 1
            else:
                can_red[y] = True
                num_ball[x] -= 1
                num_ball[y] += 1
        else:
            num_ball[x] -= 1
            num_ball[y] += 1
    
    # print(can_red)
    # print(num_ball)
    print(sum(can_red))

main()
