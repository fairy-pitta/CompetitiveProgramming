from itertools import product
def main():
    N, M, X = map(int, input().split())
    to_buy = list(product((0,1), repeat=N))

    price = []
    books = []
    ans = 10**18

    for _ in range(N):
        l = list(map(int, input().split()))
        price.append(l[0])
        books.append(l[1:])
    
    for i in to_buy:
        cost = 0
        levels = [(-X) for _ in range(M)]
        for j in range(len(i)):
            if i[j] == 1:
                cost += price[j]
                for algo in range(M):
                    levels[algo] += books[j][algo]
        
        flag = True
        for understanding in levels:
            if understanding < 0:
                flag = False
        
        if flag:
            ans = min(ans, cost)
        else:
            continue 
    
    if ans == 10**18:
        print(-1)
    else:
        print(ans)


main()
