def main():
    S = list(input())
    for i in range(len(S)):
        for j in range(i, len(S)):
            bef_i = S[:i]
            aft_j  =S[j:]
            if "".join(bef_i + aft_j) == "keyence":
                return True
    
    return False

if main():
    print("YES")
else:
    print("NO")