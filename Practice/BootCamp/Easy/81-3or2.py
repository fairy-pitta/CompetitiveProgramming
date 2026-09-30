
def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for num in a:
        while True:
            if num%2==0:
                num //= 2
                ans += 1
            else:
                break 
    print(ans)
main()

