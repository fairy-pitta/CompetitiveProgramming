def main():
    N = int(input())

    if N % 2 == 1:
        return 0
    else:
        ans = 0
        N //= 2
        while True:
            N //= 5
            ans += N

            if N < 5:
                break 
    return ans



print(main())


# def greedy(N):
#     ans = 1
#     for i in range(N, 0, -2):
#         ans *= i
#     return ans

# cnt = 0
# for j in reversed(str(greedy(50))):
#     if j == "0":
#         cnt += 1
#     else:
#         break

# print(cnt)