
def main():
    O = list(input())
    E = list(input())
    ans = ""
    for i in range(len(O)+len(E)):
        if i%2: 
            ans += E[i//2]
        else:
            ans += O[i//2]
    print(ans)

main()
