N = int(input())
plane = [[(False) for _ in range(100)] for _ in range(100)]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    for y in range(100):
        for x in range(100):
            if a<=x<b and c<=y<d:
                plane[y][x] = True

ans = 0
for i in range(100):
    ans += sum(plane[i])

print(ans)