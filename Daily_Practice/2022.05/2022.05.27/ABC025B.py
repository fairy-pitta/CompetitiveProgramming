def main():
    N = int(input())
    note = []
    for _ in range(N):
        x = list(input())
        note.append(x)
    #print(note)
    ans = 0
    for count in range(N):
        if count == 0:
            ans += note[0].count('x')
            ans += note[0].count('o')
            #print(ans)
        else:
            for check in range(9):
                if note[count][check] == 'o':
                    if note[count-1][check] != 'o':
                        ans += 1
                    else:
                        continue 
                elif note[count][check] == "x":
                    ans += 1
                else:
                    continue 
    
    return ans 

print(main())
                        

