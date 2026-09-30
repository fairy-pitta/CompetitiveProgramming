
def main():
    W, H, N = map(int, input().split())
    x_upper = W
    x_lower = 0
    y_upper = H
    y_lower = 0

    for _ in range(N):
        x, y, a = map(int, input().split())
        if a == 1:
            x_lower = max(x_lower, x)
        elif a == 2:
            x_upper = min(x_upper, x)
        elif a == 3:
            y_lower = max(y_lower, y)
        else:
            y_upper = min(y_upper, y)
    
    # print(x_upper, x_lower, y_upper, y_lower)
    x_range = r if (r := x_upper - x_lower) > 0 else 0
    y_domain = d if (d := y_upper - y_lower) > 0 else 0

    print(x_range*y_domain)


main()