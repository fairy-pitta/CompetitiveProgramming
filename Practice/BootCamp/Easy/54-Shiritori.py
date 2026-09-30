def main():
    N = int(input())
    last_letter = 0
    said_word = set()
    for i in range(N):
        w = str(input())
        if i == 0:
            last_letter = w[-1]
            said_word.add(w)
        else:
            if last_letter == w[0] and w not in said_word:
                last_letter = w[-1]
                said_word.add(w)
                continue 
            else:
                return False
    
    return True 

if main():
    print("Yes")
else:
    print("No")
