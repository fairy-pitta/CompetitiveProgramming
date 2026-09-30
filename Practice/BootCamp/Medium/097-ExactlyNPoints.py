def main():
    N = int(input())
    ans = []
    num = 1
    cnt = 0
    while True:
        cnt += num
        ans.append(num)
        if cnt >= N:
            break 
        num += 1
    
    if cnt > N:
        ans.remove(cnt-N)
    
    for i in ans:
        print(i)
    

main()
        

