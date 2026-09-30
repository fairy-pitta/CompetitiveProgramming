
def main():
    N, x = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    ans = 0

    if x > sum(a):
        return N-1

    for i in range(N):
        if x >= a[i]:
            x -= a[i]
            ans += 1
        else:
            break 
    
    return ans

print(main())


