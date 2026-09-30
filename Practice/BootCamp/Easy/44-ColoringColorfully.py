def main():
    S = [int(i) for i in list(input())]
    odd = []
    even = []
    for idx in range(len(S)):
        if idx%2:
            odd.append(S[idx])
        else:
            even.append(S[idx])
    
    # if all even are to be black 
    even_black = sum(even) + (len(odd)-sum(odd))
    # if all odd are to be black
    odd_black = sum(odd) + (len(even)-sum(even))

    print(min(even_black, odd_black))

main()