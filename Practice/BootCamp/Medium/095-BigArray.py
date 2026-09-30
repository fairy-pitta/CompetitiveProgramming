from bisect import bisect_left

def main():
    N, K = map(int, input().split())
    li = []
    for _ in range(N):
        a, b = map(int, input().split())
        li.append([a,b])
    
    li = sorted(li)
    
    values = [0]
    for i in range(N):
        v = li[i][1]
        values.append(values[-1]+v)
    
    idx = bisect_left(values, K)
    print(li[idx-1][0])
    


main()
    

