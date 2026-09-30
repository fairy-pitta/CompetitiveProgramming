from itertools import groupby

def runLengthEncode(S: str):
    grouped = groupby(S)
    res = []
    for k, v in grouped:
        res.append((k, int(len(list(v)))))
    return res

def main():
    S = input()
    K = int(input())

    if len(set(S)) == 1:
        print((len(S)*K)//2)
        return
    
    S_next = S*2

    s_runlength = runLengthEncode(S)
    sn_runLength = runLengthEncode(S_next)

    s_cnt = 0
    sn_cnt = 0

    for i in s_runlength:
        s_cnt += i[1] // 2
    
    for j in sn_runLength:
        sn_cnt += j[1] // 2
    
    if K == 1:
        print(s_cnt)
    else:
        print(s_cnt + (sn_cnt-s_cnt) * (K-1))

main()

