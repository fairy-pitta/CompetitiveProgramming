def main():
    N = int(input())
    H = list(map(int, input().split()))

    ans = True

    for i in reversed(range(1, N)):
        if H[i] - H[i-1] >= 0:
            continue 
        elif H[i] - H[i-1] == -1:
            H[i-1] -= 1
        else:
            ans = False
            break 
    
    if ans:
        print("Yes")
    else:
        print("No")

main()


