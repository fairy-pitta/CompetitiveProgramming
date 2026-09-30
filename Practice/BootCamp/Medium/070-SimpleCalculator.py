
def main():
    x, y = map(int, input().split())
    xm = -x
    ans = 10**18

    if x + abs(x-y) == y:
        ans = min(ans, abs(x-y))
    if -(x + abs(x-y)) == y:
        ans = min(ans, abs(x-y)+1)
    if -x + abs(x-y) == y:
        ans = min(ans, abs(x-y)+1)
    if -x + abs(x-y) == -y:
        ans = min(ans, abs(x-y)+2)
    if x + abs(x+y) == y:
        ans = min(ans, abs(x+y))
    if -(x + abs(x+y)) == y:
        ans = min(ans, abs(x+y)+1)
    if -x + abs(x+y) == y:
        ans = min(ans, abs(x+y)+1)
    if -x + abs(x+y) == -y:
        ans = min(ans, abs(x+y)+2)
    
    print(ans)

main()
