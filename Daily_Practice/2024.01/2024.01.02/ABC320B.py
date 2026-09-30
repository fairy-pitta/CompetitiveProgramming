S = input()
ans = 1
for start in range(len(S)):
    for end in range(start+1, len(S)+1):
        s = S[start:end]
        if s == s[::-1]:
            ans = max(ans, len(s))

print(ans)