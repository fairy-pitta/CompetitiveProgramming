
def main():
    n, k = map(int, input().split())
    s = list(input())
    
    num_A = s.count("A")
    num_B = s.count("B")

    diff = k - num_B

    if diff == 0:
        print(0)
    elif diff > 0:
        flag = "B"
        cnt = 0
        idx = 0
        while cnt < diff:
            for i in range(n):
                if s[i] == "A":
                    cnt += 1
                idx = i
                if cnt == diff:
                    break
                

        print(1)
        print(idx+1, flag)
    else:
        flag = "A"
        cnt = 0
        idx = 0
        while cnt < abs(diff):
            for i in range(n):
                if s[i] == "B":
                    cnt += 1
                idx = i
                # print(cnt, idx)
                if cnt == abs(diff):
                    break
        print(1)
        print(idx+1, flag)

t = int(input())
for _ in range(t):
    main()

