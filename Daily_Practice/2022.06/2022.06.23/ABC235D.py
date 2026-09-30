from collections import deque 

INF = 10 ** 9
mn = 10 ** 6

def solve():
    a, N = map(int, input().split())
    # distance for N numbers 
    dist = [INF] * (mn)
    # 0 operation for 1 
    dist[1] = 0
    # prepare stack 
    que = deque()
    # start with 1 
    que.append(1)

    # print(dist)

    # while there are numbers in the stack 
    while len(que) > 0:
        # take out the leftmost 
        x = que.popleft()
        # add 1 to the operation times 
        # now this is how many times you need to 
        # operate to get to this option 
        new = dist[x] + 1
        # first operation 
        op1 = x * a
        # if it is within the range 
        if op1 < (mn):
            # the first option can be operated 
            dist[op1] = new
            # add op1 to the stack 
            que.append(op1)
        
        # print(op1, "op1")
        
        # see if operation 2 can be done
        # if x is bigger than 10 and 
        # the last digit of x is not 0 
        if x >= 10 and x % 10 != 0:
            # operation 2 
            op2 = int(str(x % 10) + str(x // 10))
            if op2 <= (mn):
            # if new is smaller than the existing dist[op2]
            # meaning new is a shorter way to reach x 
                if new < dist[op2]:
                # replace dist[op2] with new
                   dist[op2] = new 
                # add op2 to the stack 
                   que.append(op2)
            
            # print(op2, "op2")
    
    # print(dist)
    # if it changed, 
    # i.e., any operations reached N
    if dist[N] != INF:
        # return the operations 
        return dist[N]
    # else, return -1 
    else:
        return -1 

print(solve())
