S = input()
ans = 1

for start in range(len(S)):
    for end in range(start+1, len(S)):
        s = S[start:end+1]
        if s == s[::-1]:
            ans = max(ans, len(s))

print(ans)
