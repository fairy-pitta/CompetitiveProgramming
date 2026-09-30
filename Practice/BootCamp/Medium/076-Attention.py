def main():
    N = int(input())
    S = list(input())
    east = [0]
    west = [0]
    for i in S:
        if i == "E":
            east.append(east[-1]+1)
            west.append(west[-1])
        else:
            east.append(east[-1])
            west.append(west[-1]+1)
    
    ans = 10**18
    for j in range(1, N+1):
        num = east[-1] - east[j]
        num += west[j-1]
        ans = min(ans, num)
    
    print(ans)

main()