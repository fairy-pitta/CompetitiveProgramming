def InversionNumberByBubleSort(A):
    ans = []  #転倒数
    for i in range(len(A)):
        for j in range(len(A) - i - 1):
            #左側の方が小さい場合
            if A[j] > A[j + 1]:
                ans.append((A[j], A[j+1]))
                A[j], A[j + 1] = A[j + 1], A[j]
    
    return len(ans)

from itertools import permutations

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

h_perm = list(permutations(range(H)))
w_perm = list(permutations(range(W)))

ans = 10**18

for h in h_perm:
    for w in w_perm:
        flag = True
        for r in range(H):
            for c in range(W):
                if A[r][c] != B[h[r]][w[c]]: 
                    flag = False
        
        if flag:
            ans = min(ans, InversionNumberByBubleSort(list(h))+InversionNumberByBubleSort(list(w)))

print(ans if ans != 10**18 else -1)
