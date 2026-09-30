N = int(input())
D = []
for _ in range(N):
    D.append(int(input()))

ma = sum(D)

print(ma)
print(max(0, max(D) - (ma-max(D))))