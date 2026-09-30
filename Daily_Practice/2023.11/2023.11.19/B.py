
def main():
    n = int(input())
    a = list(map(int, input().split()))
    smallest = a[-1]
    cnt = 0
    for i in reversed(range(n)-1):
        idx = a[i]
        while idx > smallest: 
            if idx % 2 == 0:
                idx //= 2
            else:
                idx = idx // 2 + 1

