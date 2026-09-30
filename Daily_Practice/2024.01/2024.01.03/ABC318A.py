N, M, P = map(int, input().split())
cnt = 0
for day in range(1, N+1):
    if (day-M)%P==0:
        cnt += 1
print(cnt)