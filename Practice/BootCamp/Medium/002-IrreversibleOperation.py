def my_ceil(N, W):
    return (-(-N//W))

def main():
    S = list(input())
    idx_cnt = 0
    for i in range(len(S)):
        if S[i] == "B":
            idx_cnt += i
    
    right_cnt = 0
    for j in range(S.count("B")):
        right_cnt += len(S)-j-1
    
    print(right_cnt-idx_cnt)

main()
