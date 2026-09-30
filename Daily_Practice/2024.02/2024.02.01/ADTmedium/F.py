N, K = map(int, input().split())

med = [(0, 0)]
first_day = 0
for _ in range(N):
    a, b = map(int, input().split())
    med.append((a, b))
    first_day += b

med = sorted(med)
# print(med)
# print(first_day)
for d, n in med:
    first_day -= n
    if first_day <= K:
        print(d+1)
        break