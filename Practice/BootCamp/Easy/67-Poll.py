from collections import Counter
def main():
    N = int(input())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    
    S_counted = Counter(S)
    S_counted_sorted = S_counted.most_common()

    max_num = S_counted_sorted[0][1]
    ans = sorted([i[0] for i in S_counted.items() if i[1] == max_num])

    for i in ans:
        print(i)

main()

