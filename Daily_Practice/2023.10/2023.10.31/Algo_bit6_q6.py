
def main():
    N = int(input())
    ans = []
    for i in range(30):
        if N & (1<<i):
            ans.append(i)
    
    print(len(ans))
    print(*ans)

main()