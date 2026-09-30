from operator import itemgetter 

def main():
    N = int(input())
    restaurant = []
    for i in range(N):
        s, p = map(str, input().split())
        restaurant.append([i+1, s, int(p)])
    
    sorted_by_point = sorted(restaurant, key=itemgetter(2), reverse=True)
    sorted_by_name = sorted(sorted_by_point, key=itemgetter(1))

    for j in range(N):
        print(sorted_by_name[j][0])
main()
    