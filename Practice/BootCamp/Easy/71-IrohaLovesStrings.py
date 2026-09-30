def main():
    N, L = map(int, input().split())
    li = []
    for _ in range(N):
        s = input()
        li.append(s)
    
    li_sorted = sorted(li)
    
    ans = "".join(li_sorted)
    print(ans)

main()

    