S = input()

l = 0
u = 0

for i in S:
    if i.islower():
        l += 1
    else:
        u += 1

if u > l:
    S = S.upper()
else:
    S = S.lower()

print(S)