D = int(input())

ans = []

for x in range(1, int(D**0.5)+1):
    d = D - x**2
    y = int(d**0.5)

    ans.append(abs(x**2+y**2-D))
    ans.append(abs(x**2+(y+1)**2-D))

print(min(ans))