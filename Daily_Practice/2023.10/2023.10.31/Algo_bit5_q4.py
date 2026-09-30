
def main():
    N, S = map(int, input().split())
    Q = int(input())

    for i in range(Q):
        n, x = map(int, input().split())
        if n == 0: # Switch(x)
            S ^= (1<<x)
        else: # Check(x)
            if S & (1<<x): # = 1
                print("on")
            else: print("off")

main()