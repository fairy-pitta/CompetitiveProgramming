from itertools import permutations
from math import factorial

def calc_distance(x1,y1,x2,y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**(0.5)

def main():
    N = int(input())
    cities = []
    for _ in range(N):
        x, y = map(int, input().split())
        cities.append([x,y])

    visiting_list = list(permutations(range(N)))
    distance = 0

    for i in range(len(visiting_list)):
        dist = 0
        route = list(visiting_list[i])
        for cur in range(N-1):
            dist += calc_distance(cities[route[cur]][0], cities[route[cur]][1], cities[route[cur+1]][0], cities[route[cur+1]][1])
        
        distance += dist
    
    return distance / factorial(N)

print(main())
