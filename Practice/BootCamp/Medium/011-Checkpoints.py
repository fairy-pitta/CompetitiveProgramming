def calc_dist(x1,y1,x2,y2):
    return abs(x1-x2)+abs(y1-y2)

def main():
    N, M = map(int, input().split())
    students = [list(map(int, input().split())) for _ in range(N)]
    points = [list(map(int, input().split())) for _ in range(M)]

    for person in students:
        dist = 10**18
        checkpoint = 0
        for p in range(len(points)):
            if (d := calc_dist(person[0], person[1], points[p][0], points[p][1])) < dist:
                dist = d
                checkpoint = p+1
        print(checkpoint)
    

main()