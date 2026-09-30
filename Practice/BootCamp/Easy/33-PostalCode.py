def main():
    A, B = map(int, input().split())
    S = list(input())
    ans = True
    for i in range(len(S)):
        if i == A:
            if S[i] != "-":
                ans = False 
            else:
                continue 
        else:
            if S[i].isdigit():
                continue
            else:
                ans = False
    
    if ans:
        print("Yes")
    else:
        print("No")

main()
