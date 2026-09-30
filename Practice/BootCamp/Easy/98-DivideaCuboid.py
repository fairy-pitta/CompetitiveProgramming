def main():
    L = sorted(list(map(int, input().split())))

    all_odd = True
    for item in L:
        if not item%2:
            all_odd = False
    
    if all_odd:
        print(L[0]*L[1])
    else:
        print(0)

main()
