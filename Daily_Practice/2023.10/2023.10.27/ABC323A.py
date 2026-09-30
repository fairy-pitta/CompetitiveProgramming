S = [int(z) for z in list(input())]
ans = 0
for i in range(len(S)):
    if i%2: ans += S[i]

if not ans:
    print("Yes")
else: print("No")
