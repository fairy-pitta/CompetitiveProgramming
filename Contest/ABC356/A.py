N, L, R = map(int, input().split())

ans = [i for i in range(1, N+1)]

ans = ans[:L-1]+ans[L-1:R][::-1]+ans[R:]

print(ans)