from collections import Counter
from itertools import product 

def main():
    n = int(input())
    v = list(map(int, input().split()))

    even = []
    odd = []
    for i in range(n):
        if i%2:
            even.append(v[i])
        else:
            odd.append(v[i])
    
    ec = Counter(even).most_common()
    oc = Counter(odd).most_common()
    ans = n
    cnt = 0

    for (k1, v1), (k2, v2) in product(ec, oc):
        if k1==k2: ans = min(ans, n-v1, n-v2)
        else: ans = min(ans, n-v1-v2)
        cnt += 1
        if cnt >= 10000:
            break
    
    print(ans)

main()



                


