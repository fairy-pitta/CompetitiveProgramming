import random 
import threading 
import time


def caculate_score(data, result):
    score = 0
    for i in range(len(result)):
        a, b, c, d = result[i]
        area = (c-a) * (d-b)

        score += 1-(1-min(area, data[i][2])/max(area, data[i][2]))**2
    
    return score 



N = int(input())

data = []

for _ in range(N):
    data.append(list(map(int, input().split())))

grids = [[(False) for _ in range(10000)] for _ in range(10000)]

ans = []
for i in range(N):
    a = data[i][0]
    b = data[i][1]
    c = data[i][0] + 1
    d = data[i][1] + 1
    ans.append([a, b, c, d])
    
    for x in range(a, c):
        for y in range(b, d):
            grids[x][y] = True

def main():
    random_int = random.randint(0, N)
    random_dir = random.sample(
        [
            (0, -1, 0, 0),
            (0, 0, 1, 0),
            (-1, 0, 0, 0),
            (0, 0, 0, 1)
        ], 1
    )

    
