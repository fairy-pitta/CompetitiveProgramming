

def isColinear(x1,y1,x2,y2,x3,y3):
    x1 -= x3
    x2 -= x3
    y1 -= y3
    y2 -= y3
    if x1 * y2 == x2 * y1:
        return True
    return False 

def main():
    N = int(input())
    points = []
    for _ in range(N):
        points.append(list(map(int, input().split())))
    
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if not isColinear(points[i][0], points[i][1], points[j][0],points[j][1], points[k][0], points[k][1]):
                    cnt += 1
    
    print(cnt)

main()