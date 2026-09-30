N = int(input())

def greedy(N):
    a = 1
    for i in range(2, N+1, 2):
        a *= i

    s = list(str(a))[::-1]
    cnt = 0
    for j in s:
        if j == "0":
            cnt += 1
        else:
            break
    return cnt

# print(greedy(N))

def main(N):
    if N%2 == 1:
        return 0
    ans = 0
    div = 10
    while True:
        if N < div:
            break
        ans += N // div
        div *= 5

    return ans 

print(main(N))