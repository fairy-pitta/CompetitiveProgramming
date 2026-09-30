def check_ss(s: list) -> bool:
    if len(s)%2:
        return False
    
    mid_point = len(s)//2
    if s[:mid_point] == s[mid_point:]:
        return True
    
    return False


def main():
    S = list(input())
    for _ in range(len(S)):
        S.pop()
        if check_ss(S):
            return len(S)

print(main())
    
