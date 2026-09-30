def main():
    from operator import itemgetter
    N = int(input())
    Moji = set()
    Judge = []
    for i in range(N):
        s,t = map(str, input().split())
        t = int(t)
        if s not in Moji:
            Moji.add(s)
            Judge.append([(-1)*t, i+1])
    Ans = sorted(Judge, key = itemgetter(0,1))
    return Ans[0][1]

print(main())
    
