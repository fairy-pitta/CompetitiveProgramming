
def main():
    N = int(input())
    possible_price = int(N // 1.08)

    for price in range(possible_price-20, possible_price+21):
        if int(price * 1.08) == N:
            print(price)
            return 
    
    print(":(")
    return

main()
        