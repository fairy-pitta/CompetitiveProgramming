
def main():
    N, A, B, C, D = map(int, input().split())
    S = list(input())
    A -= 1
    B -= 1
    C -= 1
    D -= 1

    for i in range(A, max(C,D)):
        if (A < i < C or B < i < D) and S[i] == S[i+1] == "#":
            return False
        
    if C < D:
        return True
    
    else:
        for j in range(B-1, D):
            if S[j] == S[j+1] == S[j+2] == ".":
                return True
        
    
    return False


if main():
    print("Yes")
else:
    print("No")
