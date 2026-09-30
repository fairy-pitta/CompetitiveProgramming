from itertools import combinations

def is_valid(comb, tests, K):
    for keys_used, result in tests:
        real_keys_count = sum(1 for key in keys_used if comb & (1 << (key - 1)))
        if (result == 'o' and real_keys_count < K) or (result == 'x' and real_keys_count >= K):
            return False
    return True

N, M, K = map(int, input().split())
tests = []

for _ in range(M):
    data = list(map(str, input().split()))
    num_keys = int(data[0])
    keys_used = list(map(int, data[1:num_keys+1]))
    result = data[-1]
    tests.append((keys_used, result))


ans = 0
for comb in range(1 << N):
    if is_valid(comb, tests, K):
        ans += 1

print(ans)
