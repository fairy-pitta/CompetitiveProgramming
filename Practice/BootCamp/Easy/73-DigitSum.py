def main():
    N = list(str(input()))

    all_nine = True 
    for i in range(1, len(N)):
        if N[i] != "9":
            all_nine = False
    
    if all_nine:
        ans = int(N[0])+9*(len(N)-1)
    else:
        ans = int(N[0])-1+9*(len(N)-1)
    
    print(ans)

    
main()