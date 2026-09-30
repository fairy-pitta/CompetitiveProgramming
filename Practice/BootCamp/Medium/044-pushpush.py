from collections import deque

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = deque([])

    if n % 2 == 0:
        for i in range(n):
            if i % 2 == 0:
                b.append(a[i])
            else:
                b.appendleft(a[i])
    else:
        for i in range(n):
            if i % 2 == 0:
                b.appendleft(a[i])
            else:
                b.append(a[i])
    
    print(*b)

main()