def main():
    N, T = map(int, input().split())
    t = list(map(int, input().split()))
    end_time = T
    total_time = T

    for i in range(1, N):
        if t[i] < end_time:
            total_time += T - (end_time - t[i])
            end_time = t[i] + T
        else:
            end_time = t[i] + T
            total_time += T
        
    print(total_time)

main()
