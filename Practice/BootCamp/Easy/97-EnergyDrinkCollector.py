def main():
    N, M = map(int, input().split())
    store = []
    for _ in range(N):
        store.append(list(map(int, input().split())))
    
    store = sorted(store)

    price = 0

    for i in range(N):
        if M >= store[i][1]:
            price += store[i][0] * store[i][1]
            M -= store[i][1]
        else:
            price += store[i][0] * M
            break
    
    print(price)

main()