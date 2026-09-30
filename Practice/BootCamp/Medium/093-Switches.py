from itertools import product

def main():
    N, M = map(int, input().split())
    light = []
    for _ in range(M):
        s = list(map(int, input().split()))
        light.append(s[1:])
    
    p = list(map(int, input().split()))

    li = list(product([0,1], repeat = N))
    
    ans = 0
    for i in li:
        flag = True
        for e in range(M):
            cnt = 0
            connected_switch = light[e]
            for switch in connected_switch:
                if i[switch-1] == 1:
                    cnt += 1
            if cnt % 2 != p[e]:
                flag = False
        
        if flag:
            ans += 1
    
    print(ans)           



main()