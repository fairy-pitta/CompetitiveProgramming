from collections import Counter

def main():
    N = int(input())
    A = list(map(int, input().split()))
    C = sorted(Counter(A).items(), reverse=True)
    ans = []
    for i in C:
        if i[1] >= 4:
            ans.append(i[0])
            ans.append(i[0])
        elif i[1] >= 2:
            ans.append(i[0])
    
    if len(ans) < 2:
        print(0)
    else:
        print(ans[0]*ans[1])

main()


