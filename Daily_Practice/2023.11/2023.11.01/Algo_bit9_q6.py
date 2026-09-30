
def get_list(N):

    ans = 0

    for i in range(N):
        ans += (1<<i)
    
    print(ans)
    


def main():
    N, X = map(int, input().split())
    Q = int(input())
    for i in range(Q):
        f, v = map(int, input().split())
        if f == 0: # Insert(x)
            X |= (1<<v)
        elif f == 1: # Delete(x)
            X &= ~(1<<v)
        else: # Find(x)
            # get_list(X)
            if X & (1<<v) > 0:
                print("Yes")
            else: print("No")

main()