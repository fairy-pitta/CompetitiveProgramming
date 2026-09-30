from collections import defaultdict

M = int(input())
s1 = input()*3
s2 = input()*3
s3 = input()*3

cnt = 10**18

for f in range(M*3):
    for s in range(M*3):
        for t in range(M*3):
            if (s1[f]==s2[s]==s3[t]) and (f!=s and f!=t and s!=t):
                cnt = min(cnt, max(f,t,s))


print(cnt if cnt < 10**18 else -1)




