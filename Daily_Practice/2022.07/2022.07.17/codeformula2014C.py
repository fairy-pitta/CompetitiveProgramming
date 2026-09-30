import string
s = list(input())
alphabet = set(string.ascii_lowercase)

ans = []
for i in range(len(s)):
    if s[i] == "@":
        li = ""
        while True:
            for j in range(i+1, len(s)):
                if s[j] not in alphabet:
                    break 
                else:
                    li += s[j]
    else:
        continue
ans.sort()
for letters in ans:
    print(letters)

    