def main():
    N = int(input())
    z = []
    w = []
    for _ in range(N):
        x, y = map(int, input().split())
        z.append(x+y)
        w.append(x-y)
    
    print(max(abs(max(z)-min(z)), abs(max(w)-min(w))))

main()
