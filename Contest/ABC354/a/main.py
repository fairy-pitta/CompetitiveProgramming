H = int(input())

ans = 0
height = 0
for i in range(100):
    height += 2**i
    if height > H:
        ans = i+1
        break

print(ans)