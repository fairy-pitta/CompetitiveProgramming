N = int(input())

from operator import itemgetter 

giants = []
for _ in range(N):
    a, b = map(int, input().split())
    giants.append([a, b, b-a])

sorted_giants = sorted(giants, key=itemgetter(2), reverse=True)

ans = 0

for i in range(N):
    if i == 0:
        ans += sorted_giants[i][0]
        ans += sorted_giants[i][2]
    else:
        ans += sorted_giants[i][0]

print(ans)

N = int(input())

head_size = -1
ans = 0

for _ in range(N):
    a, b = map(int, input().split())
    # 肩の高さを答えに追加
    ans += a 

    # 頭の大きさを計算
    head_size = max(head_size, b-a)

print(ans+head_size)