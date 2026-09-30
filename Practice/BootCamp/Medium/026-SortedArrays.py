# 尺取り

from collections import deque
def main():
    N = int(input())
    A = deque(list(map(int, input().split())))

    que = deque([])
    flag = 0 # 0: Undetermined, 1: Increasing, 2: Decreasing 
    cnt = 0

    cur = A.popleft()

    while True:

        if len(A) == 0:
            break

        next = A.popleft()

        # print(flag, cur, next)
        if flag == 0: # Undetermined 
            if cur < next: # incresing 
                flag = 1 
                que.append(cur)
                cur = next
            elif cur == next:
                que.append(cur)
                cur = next 
            else:
                # cur > next # decresing 
                flag = 2
                que.append(cur)
                cur = next 
        
        elif flag == 1: # increasing 
            if cur <= next: # increasing 
                que.append(cur)
                cur = next
            else:
                cnt += 1
                que.append(cur)
                cur = next
                flag = 0
                # print(que, "inc")
        
        else:
            # flag == 2 decreasing 
            if cur >= next: 
                que.append(cur)
                cur = next
            else:
                cnt += 1
                que.append(cur)
                cur = next
                flag = 0
                # print(que, "dec")
    
    print(cnt+1)

main()
    

    

            



