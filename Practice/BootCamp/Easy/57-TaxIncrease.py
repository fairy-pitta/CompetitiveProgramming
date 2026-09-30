def original_price(price :int, tax: int) -> list:
    p = int(price // (tax/100))
    price_list = []
    for possible_price in range(p-100, p+100):
        if possible_price * tax // 100 == price:
            price_list.append(possible_price)
    return price_list

def main():
    A, B = map(int, input().split())
    A_list= original_price(A, 8)
    B_list = original_price(B, 10)
    for price in A_list:
        if price in set(B_list):
            return price 
    
    return "-1"

print(main())

