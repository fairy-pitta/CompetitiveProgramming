
def main():
    N, K = map(int, input().split())
    A = set(list(map(int, input().split())))
    m = 0

    for i in range(K):
        if i in A:
            m = i+1
        else:
            break 
    
    print(m)
    

main()

