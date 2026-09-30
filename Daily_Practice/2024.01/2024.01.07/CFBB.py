N = list(str(input()))[::-1]
odd = 0
even = 0
for i in range(len(N)):
    if i%2: even += int(N[i])
    else: odd += int(N[i])

print(even, odd)

