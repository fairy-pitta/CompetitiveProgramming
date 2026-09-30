from operator import itemgetter 

N = int(input())
mountains = []
for _ in range(N):
    s, t = map(str, input().split())
    mountains.append([int(t), s])

mountains = sorted(mountains, key=itemgetter(0))
# print(mountains)
print(mountains[-2][1])