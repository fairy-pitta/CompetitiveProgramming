A, B = map(int, input().split())
B *= 1000
ans = round(B / A)
ans = str(ans)
if len(ans) <= 3:
    ans = "0." + str(ans).zfill(3)
else:
    ans = ans[0] + "." + ans[1:]
print(ans)