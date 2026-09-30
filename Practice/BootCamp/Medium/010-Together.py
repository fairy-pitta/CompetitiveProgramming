from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i in A:
        d[i] += 1
    
    ans = 0
    key_list = list(d.keys())
    
    for k in key_list:
        cnt = d[k] + d[k-1] + d[k+1]
        ans = max(ans, cnt)
    
    print(ans)

main()

