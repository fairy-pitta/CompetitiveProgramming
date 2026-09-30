def main():
    L, R = map(int, input().split())
    m = 10 ** 9
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            m = min(m, (i*j) % 2019)
            if (i*j) % 2019 == 0:
                return 0
    
    return m
print(main())
