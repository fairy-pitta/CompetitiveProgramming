# https://atcoder.jp/contests/code-festival-2015-morning-easy/tasks/cf_2015_morning_easy_c


N, K, M, R = map(int, input().split())

score = []
for _ in range(N-1):
    score.append(int(input()))

score = sorted(score, reverse=True)

if sum(score[:K]) >= R*K:
    print(0)
elif R*K - sum(score[:K-1]) <= M:
    print(R*K - sum(score[:K-1]))
else:
    print(-1)


