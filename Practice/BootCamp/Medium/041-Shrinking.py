
def main():
    S = list(input())
    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
    ans = 10**18

    for letter in alphabet_list:
        cnt = 0
        turn = 0
        for i in range(len(S)):
            if S[i] == letter:
                turn = max(turn, cnt)
            else:
                cnt += 1
        
        turn = max(turn, cnt)
        ans = min(ans, turn)
    print(ans)

main()


# a_ans
ans = 1000
s = input()
for i in range(26):
    cnt = 0
    samax = 0
    for j in s:
        
        if chr(97+i)==j:
            samax = max(samax,cnt)
            cnt = 0
        else:
            cnt += 1
    samax = max(samax,cnt)
    # print(i,samax,chr(i+97))
    ans = min(ans,samax)
print(ans)