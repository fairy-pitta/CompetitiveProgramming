li = set(list(map(int, input().split())))

if len(li) == 2:
    print(6-sum(li))
else:
    print(-1)

