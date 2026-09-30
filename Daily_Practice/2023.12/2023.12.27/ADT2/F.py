from bisect import bisect_right, bisect_left

N = int(input())
S = input()
W = list(map(int, input().split()))

children = []
adults = []

for i in range(len(W)):
    if S[i] == "1":
        adults.append(W[i])
    else:
        children.append(W[i])

adults = sorted(adults)
children = sorted(children)
ans = 0
W.append(0)
W.append(10**9+1)
for i in W:
    child_num = bisect_left(children, i)
    adults_num = bisect_left(adults, i)
    cnt = child_num + (len(adults)-adults_num)
    ans = max(ans, cnt)

print(ans)