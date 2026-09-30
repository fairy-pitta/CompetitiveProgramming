def greedy(l, num):
    pos = [(1) for _ in range(len(l))]
    for _ in range(num):
        new_pos = [(0) for _ in range(len(l))]
        for j in range(len(l)):
            if l[j] == "L":
                new_pos[j-1] += pos[j]
            else:
                new_pos[j+1] += pos[j]
        pos = new_pos
    return pos

S = list(input())

print(*greedy(S, 100))

