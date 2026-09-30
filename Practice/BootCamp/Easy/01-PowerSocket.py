# 1m32s
from math import ceil

def main():
    A, B = map(int, input().split())
    if B == 1:
        return 0
    for i in range(1, 20):
        if A*i-(i-1) >= B:
            return i

print(main())
