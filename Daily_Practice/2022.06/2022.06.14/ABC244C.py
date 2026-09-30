N = int(input())

pool = [i for i in range(2, 2*N+2)]

def main(N):
    while True:
        if len(pool) <= 0:
            break 
        for turn in range(1, 2*N+2):
            if turn == 1:
                print(1)
            else:
                s = int(input())
                pool.remove(s)
                print(pool[0])
                del(pool[0])
                
main(N)



