def main():
    N = int(input())
    Light = []

    # [Light, idx]
    for i in range(N):
        a = int(input())
        Light.append([a-1, i])
    
    cur_idx = 0
    cur_light = Light[0][0]
    cnt = 0
    
    while True:

        if cur_idx == 1:
            break
        if cnt > N:
            break

        cur_idx = Light[cur_light][1]
        cur_light = Light[cur_light][0]
        cnt += 1
    
    if cnt > N:
        print(-1)
    else:
        print(cnt)
        
main()
