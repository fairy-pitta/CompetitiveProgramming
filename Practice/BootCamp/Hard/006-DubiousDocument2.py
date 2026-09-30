S = input()
T = input()

ans = []
for l in range(len(S)-len(T)+1):
    flag = True
    for t in range(len(T)):
        s_idx = l+t
        if S[s_idx] != T[t] and S[s_idx] != "?":
            flag = False
    
    if flag: 
        new_s = S[:l] + T + S[l+t+1:]
        new_s = new_s.replace("?", "a")
        ans.append(new_s)

if len(ans) == 0:
    print("UNRESTORABLE")
else:
    print(min(ans))
        
