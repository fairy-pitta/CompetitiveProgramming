from itertools import combinations

N = int(input())
ans = 0

group = set()
for i in range(1, N+1):
    group.add(i)

for v in combinations(group, 2):
    first, second = v
    if ((first * second) ** (0.5)).is_integer():
        ans += 2

ans += N

print(ans)

