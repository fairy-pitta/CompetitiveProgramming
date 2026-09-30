N = int(input())

username = []
rate = 0

for _ in range(N):
    name, cost = map(str, input().split())
    username.append(name)
    rate += int(cost)

username.sort()

winner = rate % N

print(username[winner])