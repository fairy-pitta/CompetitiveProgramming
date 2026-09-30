
def main():
    n = int(input())
    A = list(map(int, input().split()))
    from collections import deque 
    dq = deque() 
    for num in range(1,n+1):
        if num % 2 == 1:
            dq.append(A[num-1])
        else:
            dq.appendleft(A[num-1])
    
    dq_list = list(dq)
    ans = 0 


    if n % 2 == 0:
        ans = dq_list
    else:
        dq_list.reverse()
        ans = dq_list
    
    print(*ans)

main()


    