def primes_list(n):
    prime_flag = [1] * (n + 1)
    prime_flag[0] = 0
    prime_flag[1] = 0

    i = 2
    while i * i <= n:
        if prime_flag[i]:
            for j in range(2 * i, n + 1, i):
                prime_flag[j] = 0
        i += 1
    return [i for i in range(n + 1) if prime_flag[i]]

li = primes_list(10**5)
li_bool = [0]
li_set = set(li)

for i in li:
    if (i+1) // 2 in li_set:
        li_bool.append(li_bool[-1]+1)
    else:
        li_bool.append(li_bool[-1])


from bisect import bisect_right, bisect_left

# print(li[:10])
# print(li_bool[:10])

def main():
    Q = int(input())
    for _ in range(Q):
        l, r = map(int, input().split())
        left_idx = bisect_left(li, l)
        right_idx = bisect_right(li, r)
        # print(right_idx, left_idx)
        print(li_bool[right_idx] - li_bool[left_idx])

main()  



    