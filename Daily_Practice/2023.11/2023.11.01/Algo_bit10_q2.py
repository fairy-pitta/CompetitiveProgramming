
def main():
    N, V = map(int, input().split())
    A = list(map(int, input().split()))
    flag = False

    for i in range(2**N):
        ans = 0
        for j in range(N):
            if i & (1<<j) > 0:
                ans += A[j]
        if ans == V:
            flag = True
    
    if flag:
        print("Yes")
    else:
        print("No")

main()
