def main():
    S = list(input())
    T = list(input()) * 2

    ans = False
    for i in range(len(S)):
        if T[i:i+len(S)] == S:
            ans = True
    
    if ans:
        print("Yes")
    else:
        print("No")

main()

