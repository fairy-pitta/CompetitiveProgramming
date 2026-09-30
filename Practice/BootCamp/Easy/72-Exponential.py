def main():
    X = int(input())
    max_num = 1
    
    if X <= 3:
        print(max_num)
        return 
    
    cnt = 0
    for i in range(2, X):
        n = i
        while True:
            n *= i
            cnt += 1
            if n <= X:
                max_num = max(max_num, n)
            else:
                break 

            if cnt > 100:
                break 
    
    print(max_num)

main()
