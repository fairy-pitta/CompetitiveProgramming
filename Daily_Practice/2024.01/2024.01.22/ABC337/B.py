S = input()
placeholder = ["A", "B", "C"]
flag = True

for i in range(len(S)):
    if S[i] == "B":
        if "A" in set(S[i:]) :
            flag = False
    elif S[i] == "C":
        if "A" in set(S[i:]) or "B" in set(S[i:]):
            flag = False 

if flag:
    print("Yes")
else:
    print("No")


    