def main():
    H, W = map(int, input().split())
    chocolate = []
    for intake in range(H):
        a = list(map(int, input().split()))
        chocolate.append(a)
    
    field = [["B" for i in range(W)] for j in range(H)]
    ans = "Yes"


    for row in range(H):
        s = sum(chocolate[row])
        share = s // 2
        for lets_see in range(W):
            can = False
            if chocolate[row][:lets_see] == share:
                for paint in range(lets_see):
                    field[paint] = "A"
                    can = True
            
            if can == False:
                ans = "No"
                break
    
    print(ans)

    for row in range(H):
        print("".join(row))

main()
                