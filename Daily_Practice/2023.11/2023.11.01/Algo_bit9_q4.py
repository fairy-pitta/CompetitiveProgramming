
def get_list():
    N = int(input())

    ans = 0

    for i in range(N):
        ans += (1<<i)
    
    print(ans)
    
    
get_list()
