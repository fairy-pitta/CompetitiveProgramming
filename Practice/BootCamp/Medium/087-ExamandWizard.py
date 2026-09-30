from bisect import bisect_right

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cnt = 0
    needs_deducting = []
    needs_increasing = 0

    for i in range(N):
        if A[i] < B[i]:
            cnt += 1
            needs_increasing += B[i]-A[i]
        else:
            needs_deducting.append(A[i]-B[i])
    
    if needs_increasing == 0:
        return print(0)
    
    needs_deducting = sorted(needs_deducting, reverse = True)
    li = [0]
    for i in range(len(needs_deducting)):
        li.append(li[-1]+needs_deducting[i])
    idx = bisect_right(li, needs_increasing)
    if idx == len(li)-1:
        return print(-1)
    cnt += idx-1


    print(cnt)

main()


