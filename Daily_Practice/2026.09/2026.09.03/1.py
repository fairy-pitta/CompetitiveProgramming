s = str(input())
w = int(input())
count = w-1
ans = ""
for i in s:
    if count == w-1:
        ans += i 
        count = 0
    else:
        count += 1

print(ans)

