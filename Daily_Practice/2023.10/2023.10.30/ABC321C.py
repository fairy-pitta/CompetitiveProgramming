from itertools import product 

def make_list():
    ans = []
    li = list(product((0,1), repeat = 10))
    for i in range(len(li)):
        if sum(li[i]) == 0 or sum(li[i]) == 10:
            break
        item = []
        for j in range(10):
            print(li[i][j])
            if li[i][j] == 1:
                item.append(j)
        print(item)
        item = sorted(item, reverse = True)
        num = int(''.join(map(str, item)))
        ans.append(num)
        print(num)
        
    
    ans = sorted(ans)

    return ans

A = make_list()
print(A)

