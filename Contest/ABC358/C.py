from itertools import combinations

N, M = map(int, input().split())

store = []
for _ in range(N):
    store.append(input())

goal = 'o' * M

min_stores = 10**18

for r in range(1, N + 1):
    for comb in combinations(range(N), r):
        collected_items = ['x'] * M
        for i in comb:
            for j in range(M):
                if store[i][j] == 'o':
                    collected_items[j] = 'o'
        if ''.join(collected_items) == goal:
            min_stores = min(min_stores, r)

print(min_stores)
