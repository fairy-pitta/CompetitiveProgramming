N = int(input())

data = []

for _ in range(N):
    data.append(list(map(int, input().split())))


ans = []

for i in range(N):
    ans.append([data[i][0], data[i][1], data[i][0]+1, data[i][1]+1])

for j in ans:
    print(*j)
