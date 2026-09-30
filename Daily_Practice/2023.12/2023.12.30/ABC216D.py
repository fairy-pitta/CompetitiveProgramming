from collections import deque, defaultdict 

def main():
    N, M = map(int, input().split())
    balls = []
    cnt = [(0) for _ in range(N+1)]
    d = defaultdict(list)
    two = deque([])
    for i in range(M):
        _ = int(input())
        a = list(map(int, input().split()))
        for item in a:
            d[item].append(i)
        cnt[a[0]] += 1
        if cnt[a[0]] == 2:
            two.append(a[0])
        balls.append(deque(a))
    
    while True:

        if two:
            color = two.popleft()
            for b in d[color]:
                balls[b].popleft()
                cnt[color] = 0
                
                if balls[b]:
                    cnt[balls[b][0]] += 1
                    
                    if cnt[balls[b][0]] == 2:
                        two.append(balls[b][0])
            
        if not two:
            break 
    
    if sum(cnt) == 0:
        print("Yes")
    else:
        print("No")
main()
        
