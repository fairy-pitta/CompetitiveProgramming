N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

right = defaultdict(int)
for i in range(2, N):
    right[A[i]] += 1

left = defaultdict(int)
left[A[0]] += 1

s = left[A[0]] * right[A[0]]
ans = 0
for i in range(1, N-1):
    print(ans, i, left, right)
    ans += s
    num = A[i]
    s -= left[num] * right[num]
    left[num] += 1
    right[A[i+1]] -= 1
    s += left[num] * right[num]

print(ans)

