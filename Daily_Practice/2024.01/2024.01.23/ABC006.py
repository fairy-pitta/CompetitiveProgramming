n = int(input())
MOD = 10007
li = [0, 0, 1]

for i in range(3, 10**6+1):
    li.append((li[i-3]+li[i-2]+li[i-1])%MOD)

# print(li)
print(li[n-1])
