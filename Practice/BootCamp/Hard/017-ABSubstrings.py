N = int(input())
a = 0
b = 0
cnt = 0

for _ in range(N):
    s = input()
    if s[0] == "B":
        b += 1
    if s[-1] == "A":
        a += 1
    cnt += s.count("AB")

print(min(a, b)+cnt)