from math import lcm

def main():
    n, m = map(int, input().split())
    s = input()
    t = input()
    l = lcm(n,m)
    div_n = l // n
    div_m = l // m
    r = lcm(div_n, div_m)
    time_n = r // div_n
    time_m = r // div_m

    ncur = 0
    mcur = 0
    flag = True
    while True:
        if ncur*div_n+1 > l or mcur*div_m+1 > l:
            break 
        # print(ncur, mcur)
        if s[ncur] != t[mcur]:
            flag = False
            break
        ncur += time_n
        mcur += time_m
    
    if flag:
        print(l)
    else:
        print(-1)

main()

