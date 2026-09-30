from operator import itemgetter
def main():
    N, W = map(int, input().split())
    cheese = []
    for _ in range(N):
        a, b = map(int, input().split())
        cheese.append([a, b])
    cheese = sorted(cheese, key = itemgetter(0), reverse=True)
    rem = W 
    score = 0
    while rem > 0:
        for i in range(N):
            if cheese[i][1] <= rem:
                rem -= cheese[i][1]
                score += cheese[i][0] * cheese[i][1]
            else:
                




