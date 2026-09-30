from bisect import bisect_left

def main():
    N = int(input())
    li = []
    for i in range(N):
        a = list(map(int, input().split()))
        sum_a = sum(a)
        li.append(sum_a)
    
    li.sort()
    ans = bisect_left(li, 20)
    return ans 

print(main())

