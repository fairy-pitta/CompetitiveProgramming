class BIT:

    #初期化
    def __init__(self, n):
        self.size=n
        self.tree = [0] * (n+1) #1-indexのリストで管理
    
    #加算
    def add(self, i,x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i       #LSBの計算
    #インデックス0からiまでの総和を計算
    def sum(self, i):
        total = 0
        while i >0:
            total += self.tree[i]
            i -= i & -i       #LSBの計算
        
        return total

MOD = 10**9 + 7

def InversionNumberByBIT(A):
    ans = 0
    Bit = BIT(len(A)) #Binary Indexed Tree
    for i in range(len(A)):
        ans += i - Bit.sum(A[i])
        Bit.add(A[i], 1) #自分の位置を1にする
    return ans

N, K = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0

for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            cnt += 1

num = InversionNumberByBIT(A)

ans = 0
for i in range(K):
    ans += num
    ans += i*cnt
    ans %= MOD


print(ans)


