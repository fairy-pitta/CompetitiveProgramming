def main():
    s = str(input())
    flag = True
    for i in range(len(s)):
        if i == 0:
            if s[i] != "<":
                flag = False 
        elif i == len(s)-1:
            if s[i] != ">":
                flag = False 
        else:
            if s[i] != "=":
                flag = False 

    return flag 

if main():
    print("Yes")
else:
    print("No")
