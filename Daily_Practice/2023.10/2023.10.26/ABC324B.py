N = int(input())

flag = 0
for i in range(1000):
    for j in range(1000):
        if 2**i * 3**j == N:
            flag = 1
            break

if flag:
    print("Yes")
else:
    print("No")