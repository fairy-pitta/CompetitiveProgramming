def main():
    N = int(input())
    m1 = 0
    m2 = 0
    T = []
    for _ in range(N):
        t = int(input())
        T.append(t)
    T.sort(reverse = True)

    for meat in range(N):
        if m1 >= m2:
            m2 += T[meat]
        else:
            m1 += T[meat]
    
    ans = max(m1, m2)
    return ans 

print(main())


