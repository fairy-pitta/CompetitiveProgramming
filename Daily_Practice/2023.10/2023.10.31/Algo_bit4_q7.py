

def main():
    N, S = map(int, input().split())
    Q = int(input())
    for i in range(Q):
        x, i = map(int, input().split())
        if x: # 1 = Check 
            if not (S & 1<<i): # = 0
                print("off")
            else:
                print("on")
        else:
            S = (S | 1<<i)

main()
                