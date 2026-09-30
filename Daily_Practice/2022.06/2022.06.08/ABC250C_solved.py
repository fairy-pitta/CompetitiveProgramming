def main():
    N, Q = map(int, input().split())
    A = list(range(N+1))
    idx = list(range(N+1)) # element in ith in A

    for _ in range(Q):
        x = int(input())
        where_x_is = idx[x] # where x is in A
        # where_x_goes: literally where x goes to after the swapping 
        # if x is at the end 
        if where_x_is == N:
            # x goes to the lft 
            where_x_goes = where_x_is - 1 
        # if not 
        else:
            # x goes to the right 
            where_x_goes = where_x_is + 1 
        
        # what was in where_x_goes position originally? 
        wheres_y = A[where_x_goes]
        # swap 
        A[where_x_goes], A[where_x_is] = A[where_x_is], A[where_x_goes]
        # x moves to where_x_goes 
        idx[x] = where_x_goes
        # y moves to where x was 
        idx[wheres_y] = where_x_is 
    # print A, but not A[0]
    print(*A[1:])

main()



        

