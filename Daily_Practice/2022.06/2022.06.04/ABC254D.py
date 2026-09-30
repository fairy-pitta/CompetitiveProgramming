def divisor(n):
    sq = n**0.5
    border = int(sq)
    table = []
    bigs = []
    for small in range(1, border+1):
        if n%small == 0:
            table.append(small)
            big = n//small
            bigs.append(big)
    if border == sq:#nが平方数
        bigs.pop()
    table += reversed(bigs)
    return table


from bisect import bisect_right

def main():
    N = int(input())
    li = [1]

    while True:
        if max(li) >= (N**2):
            break
        for i in range(2, 10**3):
            li.append(i * i)
            if max(li) >= (N**2):
                break

    ans = 0
    for element in li:
        sq = element**0.5
        border = int(sq)
        a = []
        bigs = []
        for small in range(1, border+1):
            if element%small == 0:
                a.append(small)
                big = element//small
                bigs.append(big)
            if border == sq:#nが平方数
                bigs.pop()
        a += reversed(bigs)
        
        index = bisect_right(a, N)
        if len(a) % 2 == 0:
            x = index - (len(a) - index)
            ans += x // 2
        else:
            x = index - (len(a) - index)
            ans += x // 2
            ans += 1
    return ans 


print(main())
