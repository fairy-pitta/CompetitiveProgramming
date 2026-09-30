from collections import deque 

def main():
    T = int(input())
    for i in range(T):
        n, d, k = map(int, input().split())
        grid = [(False) for _ in range(n)]
        grid[0] = True 
        colored = [0]
        a = 0
        x = 0
        for _ in range(n-1):
            x = (a+d)%n
            while True:
                if not grid[x]:
                    grid[x] = True
                    colored.append(x)
                    break 
                x = (x+1)%n
            a = x
        print(colored[k-1])

main()





