N = int(input())
A = list(map(int, input().split()))
from collections import defaultdict

d = defaultdict(int)
for i in A:
    d[i] += 1


def main():
    if N % 2 == 1:
        if d[0] != 1:
            return False
        else:
            for v in range(2, N, 2):
                if d[v] != 2:
                    return False
        
        return True
    else:
        for v in range(1, N, 2):
            if d[v] != 2:
                return False
        
        return True

if main():
    print(pow(2, (N//2), 10**9+7))
else:
    print(0)
