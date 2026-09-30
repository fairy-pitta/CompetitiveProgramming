
def main():
    N, S = map(int, input().split())
    Q = int(input())
    for i in range(Q):
        x, i = map(int, input().split())
        if x == 0: # On(x), switch on 
            S = S | (1<<i)
        elif x == 1: # Off(x), switch off 
            S = S & ~(1<<i)
        else: # Check(x), is the switch on 
            if S & (1<<i): # = 1 
                print("on")
            else:
                print("off")

main()
                