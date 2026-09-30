N  = int(input())
li = [[] for _ in range(N+1)]
for row in range(N+1):
    for num in range(row):
        if num == 0 or num == (row-1):
            li[row].append(1)
        else:
            li[row].append(li[row-1][num-1] + li[row-1][num])

for ans in range(N+1):
    print(*li[ans])


