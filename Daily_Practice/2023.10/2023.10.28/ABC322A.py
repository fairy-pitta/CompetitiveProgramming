N = int(input())
S = list(input())
ans = -1
for i in range(N-2):
    if S[i] == "A" and S[i+1] == "B" and S[i+2] == "C":
        ans = i+1
        break 

print(ans)

