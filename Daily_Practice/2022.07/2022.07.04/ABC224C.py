from math import sqrt
# 2点間の距離を求める
def dist(x1, y1, x2, y2):
    d = sqrt((x1 - x2) ** 2 + (y1 - y2)**2) 
    return d 

def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        ex, why = map(int, input().split())
        x.append(ex)
        y.append(why)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                # 各点同士の距離
                d1 = dist(x[i], y[i], x[j], y[j])
                d2 = dist(x[i], y[i], x[k], y[k])
                d3 = dist(x[k], y[k], x[j], y[j])
                li = [d1, d2, d3]
                # 最長辺
                m = max(li)
                rest = sum(li) - m
                # 最長辺以外の2辺の和＞最長辺
                if rest - m > 0:
                    ans += 1
    return ans 

def gradient(x1, y1, x2, y2):
    return (y1 - y2) // (x1-x2)

def solve():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        ex, why = map(int, input().split())
        x.append(ex)
        y.append(why)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if (y[i] - y[j]) * (x[j] - x[k]) != (y[j] - y[k]) * (x[i] - x[j]):
                    ans += 1
    
    return ans

print(solve())

    

