# 1 x c：数 x が書かれたボールを筒の右側から c 個入れる
# 2 c：筒の左側からボールを c 個取り出し、取り出したボールに書かれている数の合計を出力する

# input 
# 1 x c 
# 2 c 

# Q
# query 1 ... query_Q

from collections import deque
def main():
    Q = int(input())
    li = deque()
    for _ in range(Q):
        i = list(map(int, input().split()))
        if i[0] == 1:
            li.append([i[1], i[2]])
        else:
            c = i[1]
            ans = 0
            while c > 0:
                # print(li)
                if li[0][1] >= c:
                    ans +=  li[0][0] * c
                    li[0][1] -= c
                    c = 0
                else:
                    ans += li[0][0] * li[0][1]
                    c -= li[0][1]
                    li.popleft()
            print(ans)

main()



