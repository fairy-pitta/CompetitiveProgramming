
def main():
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    price = min(a) + min(b)
    for _ in range(M):
        x,y,c = map(int, input().split())
        price = min(price, a[x-1]+b[y-1]-c)
    print(price)

main()
