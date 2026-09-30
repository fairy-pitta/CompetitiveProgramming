from collections import defaultdict

def main():
    n = int(input())
    d = defaultdict(list)
    alphabet_letters = list('abcdefghijklmnopqrstuvwxyz')

    for _ in range(n):
        s = input()
        for i in range(26):
            d[alphabet_letters[i]].append(s.count(alphabet_letters[i]))
    
    ans = []

    for k, v in d.items():
        if len(v) == 0:
            continue
        for _ in range(min(v)):
            ans.append(k)

    ans = "".join(sorted(ans))

    print(ans)

main()
