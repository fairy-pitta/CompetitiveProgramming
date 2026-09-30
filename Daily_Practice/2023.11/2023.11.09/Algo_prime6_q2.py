from math import lcm

ans = 1
for i in range(1, 11):
    ans = lcm(ans, i)

print(ans)
    