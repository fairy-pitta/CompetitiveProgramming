N, K = map(int, input().split())
R = sorted(list(map(int, input().split())))

rate = 0

for i in reversed(range(K)):
    rate = (rate+R[-i-1]) / 2

print(rate)
