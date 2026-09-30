from copy import deepcopy

def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    ans = 102

    for i in range(101):
        li = deepcopy(A)
        li.append(i)
        new_list = sorted(li)
        score = sum(new_list) - min(new_list) - max(new_list)
        if score >= X:
            ans = i
            break 
    
    if ans > 100:
        print(-1)
    else:
        print(ans)

main()
