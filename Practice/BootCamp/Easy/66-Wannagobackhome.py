def main():
    S = list(input())
    north = S.count("N")
    south = S.count("S")
    east = S.count("E")
    west = S.count("W")

    if not ((north>0 and south>0) or (north == south == 0)):
        print("No")
        return 
    
    if not ((west>0 and east>0) or (west==east==0)):
        print("No")
        return
    
    print("Yes")
    return 

main()