N = 3
A = [1, 2, 3, 4, 5, 6]
V = [1000, 500, 100, 50, 10, 1]
L = [[1, 5, 4, 2, 3, 6], [9, 6, 2, 7, 1, 5], [32, 9, 87, 33, 41, 60]]

A = set(A)
money = 0
for i in range(len(L)):
    L[i].sort()
    ans = 0
    for j in range(len(L[i])):
        if L[i][j] not in A:
            continue 
        ans += 1
    # print(ans, "ans")
    num = len(L[i]) - ans 
    if num < len(V) and ans != 0:
        money += V[num]

print(money)

