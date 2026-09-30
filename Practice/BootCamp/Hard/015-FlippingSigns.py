N = int(input())
A = list(map(int, input().split()))

zeros = 0
minus = 0
s = 0
m = 10**18

for i in range(N):
    if A[i] < 0:
        minus += 1
    elif A[i] == 0:
        zeros += 1
    
    s += abs(A[i])
    m = min(m, abs(A[i]))

if minus % 2 == 0:
    print(s)
else:
    if zeros > 0:
        print(s)
    else:
        print(s-m*2)

