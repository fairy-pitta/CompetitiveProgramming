def main():
    C = [list(map(int, input().split())) for _ in range(3)]

    a1B = sum(C[0])
    a2B = sum(C[1])
    a3B = sum(C[2])

    b1A = sum([C[i][0] for i in range(3)])
    b2A = sum([C[j][0] for j in range(3)])
    b3A = sum([C[k][0] for k in range(3)])

    if abs(a1B-a2B)%3 != 0:
        return False
    if abs(a2B-a3B)%3 != 0:
        return False
    if abs(a1B-a3B)%3 != 0:
        return False
    if abs(b1A-b2A)%3 != 0:
        return False
    if abs(b1A-b3A)%3 != 0:
        return False
    if abs(b2A-b3A)%3 != 0:
        return False
    

    cross = C[0][0] + C[1][1] + C[2][2]
    if cross * 3 != (sum(C[0])+sum(C[1])+sum(C[2])):
        return False
    
    return True 

if main():
    print("Yes")
else:
    print("No")
    
    