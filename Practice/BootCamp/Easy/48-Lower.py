
def main():
    N = int(input())
    H = list(map(int, input().split()))
    ans_length = []

    # Corner Case 
    if N == 1:
        return 0

    cnt = 0
    left = 0
    right = 1
    while True:
        if H[left] >= H[right]:
            cnt += 1
            left += 1
            right += 1
        else:
            ans_length.append(cnt)
            cnt = 0
            left +=1
            right += 1
        
        if right == N:
            ans_length.append(cnt)
            break 
    
    return max(ans_length)


print(main())
