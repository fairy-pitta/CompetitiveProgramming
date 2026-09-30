def main():
    N, K = map(int, input().split())
    # no overlap
    s = set()

    fk = K
    cnt = 20 

    while True:
        cnt -= 1
        if cnt == 0:
            break 
        fk = min(fk, int(str(fk)[::-1]))
    
    if fk != K:
        return 0


    # reversed K
    diff = 0
    rev_K = int(str(K)[::-1])

    # if K has 0 in the end, 
    # rev_K will be shorter than K 
    # and rev_K will never be K
    if len(str(K)) != len(str(rev_K)):
        diff = len(str(K)) - len(str(rev_K))
    # print(diff)

    if N < K:
        return 0 

    # dummy K
    k = K
    while True:
        if k > N:
            break 
        s.add(k)
        k *= 10
    if K != rev_K:
        while True:
            if rev_K > N:
                break 
            s.add(rev_K)
            rev_K *= 10

    return len(s) - diff

print(main())
