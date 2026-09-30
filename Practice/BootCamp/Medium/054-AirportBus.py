
def main():
    N, C, K = map(int, input().split())
    time = []
    for i in range(N):
        t = int(input())
        time.append(t)
    
    time = sorted(time)
    p = 0
    bus_cnt = 0

    while p < N: # while there are still people
        arrival = time[p]
        cap = 0
        while p < N and time[p] <= arrival+K and cap < C:
            cap += 1
            p += 1
        bus_cnt += 1
    
    print(bus_cnt)

main()
    





    