from collections import defaultdict

def main():
    N = int(input())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for i in a:
        d[i] += 1
    
    cnt = 0
    for k, v in d.items():
        if v >= k:
            cnt += (v-k)
        else:
            cnt += v
    
    print(cnt)

main()
