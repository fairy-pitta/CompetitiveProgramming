
N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))


greedy_pair = 0
skip = 0
for i in range(0, K-1, 2):
    greedy_pair += A[i+1]-A[i]
    if i+2 < K:
        skip += A[i+2]-A[i+1]


skipped_list = [skip]


if K%2 == 0:
    print(greedy_pair)

else:
    for j in range(1, K, 2):
        # ペアを変更
        skip = skip - (A[j+1] - A[j]) + (A[j] - A[j-1])
        skipped_list.append(skip)


    if len(skipped_list) == 0:
        print(0)
    else:
        print(min(skipped_list))