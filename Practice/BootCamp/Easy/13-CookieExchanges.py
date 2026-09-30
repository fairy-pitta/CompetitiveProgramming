
def main():
    A, B, C = map(int, input().split())
    for i in range(10**6):
        if not A%2 and not B%2 and not C%2:
            A, B, C = B//2+C//2, A//2+C//2, A//2+B//2
        else:
            return i
    return -1

print(main())