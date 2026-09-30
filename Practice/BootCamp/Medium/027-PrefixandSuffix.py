
def main():
    N = int(input())
    s = list(input())
    t = list(input())

    cnt = 0
    for i in range(N):
        if s[i:] == t[:N-i]:
            cnt = max(cnt, len(s[i:]))
    
    print(2*N-cnt)

main()
