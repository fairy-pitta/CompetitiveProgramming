
from collections import defaultdict
from itertools import combinations

def main():
    N = int(input())
    d = defaultdict(int)
    for _ in range(N):
        s = input()
        d[s[0]] += 1
    
    letters = ["M", "A", "R", "C", "H"]
    letters_cmb = list(combinations(letters, 3))

    ans = 0
    for c in letters_cmb:
        if d[c[0]] > 0 and d[c[1]] > 0 and d[c[2]] > 0:
            ans += d[c[0]] * d[c[1]] * d[c[2]]
    
    print(ans)

main()

