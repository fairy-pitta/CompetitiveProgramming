# https://qiita.com/tydesign/items/ab8a5ae52eb9c50ad26a
def main():
    N = int(input())
    x = []
    y = []
    for _ in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    
    ans = 0

    for i in range(N-2):
        for j in range(i+1, N-1):
            for k in range(j+1, N):
                dx1 = x[j]-x[i]
                dx2 = x[k]-x[i]
                dy1 = y[j]-y[i]
                dy2 = y[k]-y[i]

                if dx1* dy2 == dx2 * dy1:
                    return print("Yes")
    
    return print("No")

main()