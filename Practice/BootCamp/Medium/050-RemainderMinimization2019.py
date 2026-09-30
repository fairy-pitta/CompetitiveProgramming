def main():
    L, R = map(int, input().split())

    if R-L >= 2019:
        return 0
    
    l = L%2019
    r = R%2019

    if l >= r:
        return 0
    else:
        mod_set = set()
        for i in range(l, r+1):
            mod_set.add(i)
        
        if 0 in mod_set:
            return 0
        else:
            ans = 2019
            mod_set = list(mod_set)
            for j in range(len(mod_set)):
                for k in range(j+1, len(mod_set)):
                    ans = min(ans, (mod_set[j]*mod_set[k])%2019)
            
            return ans
        
print(main())
    

