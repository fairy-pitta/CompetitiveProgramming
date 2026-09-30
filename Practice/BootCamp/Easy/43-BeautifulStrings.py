from collections import Counter
def main():
    w = list(input())
    c = Counter(w)
    ans = True
    for item in c.values():
        if item%2:
            ans = False
    
    if ans:
        print("Yes")
    else:
        print("No")

main()
