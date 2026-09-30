def main():
    X = list(input())
    N = int(input())
    for i in range(N):
        s = list(input())
        for letter in range(len(s)):
            num = ord(s[letter]) - 97
            s[letter] = X[num]
        
        print("".join(s))

main()


