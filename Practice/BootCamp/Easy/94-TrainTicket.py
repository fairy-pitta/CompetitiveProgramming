from itertools import product

def main():
    N = [int(z) for z in list(input())]
    li = list(product([-1,1], repeat=3))
    li_symbol = list(product(["-", "+"], repeat=3))

    for i in range(len(li)):
        op = list(li[i])
        symbol = list(li_symbol[i])
        cnt = N[0]
        for n in range(1,4):
            cnt += N[n]*op[n-1]
            if cnt == 7:
                ans = str(N[0])
                for k in range(3):
                    ans += symbol[k]
                    ans += str(N[k+1])
                break
    
    ans += "=7"
    print(ans)



main()
