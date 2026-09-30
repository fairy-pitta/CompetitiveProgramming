def turn(t, start):
    num = 0
    if start % 3 == 0:
        num += t // 5 * 3
        left = t % 5
        if left == 0:
            return num
        elif left == 1:
            num += 1
        elif left == 2:
            num += 2
        else:
            num += 3
    elif start % 3 == 1:
        num += t // 5 * 3
        left = t % 5
        if left == 0:
            return num
        elif left == 1:
            num += 1
        else:
            num += 2
    else:
        num += t // 5 * 3
        left = t % 5
        if left == 0:
            return num
        elif left == 4:
            num += 2
        else:
            num += 1
    
    return num

N = int(input())
H = list(map(int, input().split()))

T = 0

for i in H:
    num_turn = turn(i, T)
    T += num_turn 

print(T)