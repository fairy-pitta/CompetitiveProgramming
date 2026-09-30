from itertools import chain

def check(li: list) -> bool:

    for row in range(3):
        flag = True 
        for col in range(3):
            if not li[row][col]:
                flag = False 
        if flag: return flag 

    for col in range(3):
        flag = True 
        for row in range(3):
            if not li[row][col]:
                flag = False
        if flag: return flag
    
    if li[0][0] and li[1][1] and li[2][2]:
        return True 
    if li[0][2] and li[1][1] and li[2][0]:
        return True 
    
    return False 

def main():
    A = []
    for _ in range(3):
        a = list(map(int, input().split()))
        A.append(a)
    set_A = set(chain.from_iterable(A))
    N = int(input())
    turned = [[False, False, False] for _ in range(3)]
    for _ in range(N):
        b = int(input())
        if b in set_A:
            for row in range(3):
                for col in range(3):
                    if A[row][col] == b:
                        turned[row][col] = True
        else: continue 
    
    if check(turned):
        print("Yes")
    else:
        print("No")

main()