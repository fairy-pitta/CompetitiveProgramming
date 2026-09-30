s = list(map(str, input().split()))
N = int(input())
t = [input() for _ in range(N)]
ans = []

for i in range(len(s)):
    word = s[i]
    flag = True
    to_add = word
    for ng in t:
        if len(ng) == len(word):
            if ng.count("*") == len(ng):
                flag = False
            elif ng.count("*") > 0:
                same = True
                for letter in range(len(ng)):
                    if ng[letter] != "*" and ng[letter] != word[letter]:
                        same = False
                if same:
                    flag = False
            else:
                if ng == word:
                    flag = False
    if not flag:
        to_add = "*"*len(word)
    
    ans.append(to_add)

print(*ans)



