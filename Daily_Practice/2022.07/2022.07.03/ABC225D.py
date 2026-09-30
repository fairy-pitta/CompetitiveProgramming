def main():
    N, Q = map(int, input().split())
    head = [(-1) for _ in range(N+1)]
    tail = [(-1) for _ in range(N+1)]
    for _ in range(Q):
        s = list(map(int, input().split()))
        if s[0] == 1:
            x = s[1] 
            y = s[2] 
            tail[x] = y
            head[y] = x
        elif s[0] == 2:
            x = s[1] 
            y = s[2] 
            tail[x] = -1
            head[y] = -1
        else:
            x = s[1] 
            h = x
            while head[h] != -1:
                h = head[h]
            ans = []
            while h != -1:
                ans.append(h)
                h = tail[h]
            
            print(len(ans), *ans)
main()
                



