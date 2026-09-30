squared_number_set = set([n*n for n in range(1000)])

def main():
    N, D = map(int, input().split())
    points = []
    for _ in range(N):
        x = list(map(int, input().split()))
        points.append(x)
    
    cnt = 0
    for y in range(N):
        for z in range(y+1, N):
            distance = 0
            for d in range(D):
                distance += (points[y][d] - points[z][d])**2
            if distance in squared_number_set:
                cnt += 1
    
    print(cnt)

main()
            

