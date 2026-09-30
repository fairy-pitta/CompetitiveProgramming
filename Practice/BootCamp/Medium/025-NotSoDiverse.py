from collections import defaultdict

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for i in A:
        d[i] += 1 
    value_list = sorted(list(d.values()), reverse=True)
    ans = 0
    for j in range(len(value_list)):
        if j >= K:
            ans += value_list[j]
    
    print(ans)

main()

