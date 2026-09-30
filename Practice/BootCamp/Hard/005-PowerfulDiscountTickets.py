N, M = map(int, input().split())
A = list(map(int, input().split()))


from sortedcontainers import SortedList 
S = SortedList(A)

for _ in range(M):
    c = S.pop()
    if c == 0:
        break
    c //= 2
    S.add(c)


ans = list(S)
print(sum(ans))