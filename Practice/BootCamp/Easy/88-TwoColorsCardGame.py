from collections import defaultdict

def main():
    N = int(input())
    blue = defaultdict(int)
    for _ in range(N):
        s = str(input())
        blue[s] += 1
    M = int(input())
    red = defaultdict(int)
    for _ in range(M):
        s = str(input())
        red[s] += 1
    
    ans = 0
    for k in blue.keys():
        point = blue[k] - red[k]
        ans = max(ans, point)
    
    print(ans)

main()

    
