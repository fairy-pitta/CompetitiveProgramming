def main():
    N = int(input())
    cnt = 0
    sm = 0
    while True:
        if sm >= N:
            break
        cnt += 1
        sm += cnt 
    
    for i in range(1, cnt+1):
        if i != abs(N-sm):
            print(i)


main()
        

