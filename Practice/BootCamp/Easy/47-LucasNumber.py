def check_lucas_number(n: int) -> int:    
    lucas_number = [(0) for _ in range(87)]
    for i in range(87):
        if i == 0: 
            lucas_number[i] = 2
        elif i == 1:
            lucas_number[i] = 1
        else:
            lucas_number[i] = lucas_number[i-2]+lucas_number[i-1]
    
    return lucas_number[n]

def main():
    N = int(input())
    print(check_lucas_number(N))

main()

