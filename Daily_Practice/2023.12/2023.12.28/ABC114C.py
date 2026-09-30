from itertools import product 

def main():
    N = int(input())
    digits = len(str(N))
    cnt = 0
    for i in range(1, digits+1):
        if i < 3:
            continue 
        elif i == digits:
            li = product(("3", "5", "7"), repeat=i)
            for j in li:
                num = int("".join(j))
                if num <= N and len(set(j)) == 3:
                    cnt += 1
        else:
            li = product(("3", "5", "7"), repeat=i)
            for j in li:
                if len(set(j)) == 3:
                    cnt += 1
    
    print(cnt)

main()

