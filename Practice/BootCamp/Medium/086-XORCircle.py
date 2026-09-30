from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))

    c = sorted(list(Counter(A).items()))
    if len(c) == 1 and c[0][0] == 0:
        return True
    if len(c) == 2 and c[0][0] == 0 and c[0][1] * 2 == c[1][1]:
        return True
    if len(c) == 3 and c[0][1] == c[1][1] == c[2][1] and c[0][0]^c[1][0]^c[2][0] == 0:
        return True
    return False


if main():
    print("Yes")
else:
    print("No")