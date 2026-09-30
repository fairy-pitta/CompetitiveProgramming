from itertools import chain

def main():
    N = int(input())
    li = [[] for _ in range(N)]
    for i in range(N):
        s = list(input())
        li[s.count("x")].append(i+1)
    
    ans = list(chain(*li))
    print(*ans)

main()