def main():
    A, B, C, X, Y = map(int, input().split())
    ans = 10**18
    for ab_pizza in range(0, max(X,Y)*2+1, 2):
        price = ab_pizza * C
        a_pizza = X - ab_pizza//2
        b_pizza = Y - ab_pizza//2
        price += a_pizza * A if a_pizza >= 0 else 0
        price += b_pizza * B if b_pizza >= 0 else 0

        ans = min(ans, price)
    
    print(ans)

main()

