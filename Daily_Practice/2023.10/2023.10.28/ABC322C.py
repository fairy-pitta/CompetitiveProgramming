N, M = map(int, input().split())
A = list(map(int, input().split()))

next = A[0]
index = 0
for i in range(N-1):
    diff = next-i-1
    if diff == 0:
        print(diff)
        index += 1
        next = A[index]
    else:
        print(diff)
    
print(0)

