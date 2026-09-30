
def main():
    S = list(input())
    
    # first letter being "A"
    if S[0] != "A":
        return False 
    

    # having one "C"
    if S[2:-1].count("C") != 1:
        return False 
    
    for i in range(1, len(S)):
        if S[i] == "C" and 2 <= i <= len(S)-2:
            continue 
        elif S[i].islower():
            continue
        else:
            return False
    
    return True 

if main():
    print("AC")
else:
    print("WA")