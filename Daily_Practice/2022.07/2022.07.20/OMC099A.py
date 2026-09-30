for i in range(1, 10**9):
    one = (i + 91) * 12
    two = (i + 19) * 21
    if one == two:
        print(i)
        break 
    