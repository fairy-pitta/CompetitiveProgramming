s = list(map(str, input().split()))
# s_alt = s.replace("Left", "<").replace("Right", ">").replace("AtCoder", "A")

ans = []
for i in range(len(s)):
    if s[i] == "Left":
        ans.append("<")
    elif s[i] == "Right":
        ans.append(">")
    else:
        ans.append("A")
print(*ans)
