from collections import deque
from copy import deepcopy 

def to_tuple(a: list) -> tuple:
    return tuple(tuple(r) for r in a)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

# 存在しないキーを参照しないためにわざと辞書を使う
d = {to_tuple(A): 0}
queue = deque([A])

while len(queue) > 0:
    a = queue.popleft()

    # rowを入れ替える
    for i in range(H-1):
        b = deepcopy(a)
        b[i], b[i+1] = b[i+1], b[i]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            queue.append(b)
    
    for j in range(W-1):
        b = deepcopy(a)
        for i in range(H):
            b[i][j], b[i][j + 1] = b[i][j + 1], b[i][j]
        if to_tuple(b) not in d:
            d[to_tuple(b)] = d[to_tuple(a)] + 1
            queue.append(b)
            
print(d[to_tuple(B)] if to_tuple(B) in d else -1)

