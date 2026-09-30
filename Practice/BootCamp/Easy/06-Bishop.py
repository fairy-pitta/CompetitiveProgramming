from math import ceil

def main():
    H, W = map(int, input().split())
    if H==1 or W==1:
        return 1
    ans = 0
    # odd * odd 
    if H%2 and W%2:
        ans = (H//2+1)*(W//2+1) + (H//2)*(W//2)
    # even * odd
    elif not H%2 and W%2:
        ans = (H//2)*(W//2+1) + (H//2)*(W//2)
    # odd * even
    elif H%2 and not W%2:
        ans = (H//2+1)*(W//2) + (H//2)*(W//2)
    # even * even
    else:
        ans = (H//2)*W
    return ans 

print(main())
    
