from selectors import EpollSelector


def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0

    for flower in range(N):
        while True:
            if A[flower] % 2 == 0 or A[flower] % 3 == 2:
                ans += 1
                A[flower] -= 1
            else:
                break 
    return ans 

print(main())
    

