
def main():
    N = [int(i) for i in list(input())]
    flag = True 

    for j in range(len(N)-1):
        if N[j] <= N[j+1]:
            flag = False 
    
    return flag 

if main():
    print("Yes")
else:
    print("No")

