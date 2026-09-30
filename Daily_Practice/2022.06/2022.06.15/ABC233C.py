from collections import defaultdict

INF = (1 << 62) - 1

XY = []
def main():
    N = int(input())
    for _ in range(N):
        x, y = map(int, input().split())
        XY.append([x,y])

    S = list(input())
    
    L_max = defaultdict(lambda: -INF) # goes to left, so put it at the right end
    R_min = defaultdict(lambda: INF) # goes to right, so put it at the left end 
    
    for indx, (x, y) in zip(S, XY):
        if indx == "L":
            L_max[y] = max(x, L_max[y])
        else:
            R_min[y] = min(x, R_min[y])
    
    ans = False
    for num in L_max.keys():
        if L_max[num] > R_min[num]:
            ans = True
    
    if ans:
        print("Yes")
    else:
        print("No")

main()


    
