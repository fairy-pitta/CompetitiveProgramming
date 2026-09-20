def main():
    rows = []
    cols  = []

    for i in range(10):
        s = input()
        for j in range(10):
            if s[j] == "#":
                rows.append(i)
                cols.append(j)

    print(min(rows), max(rows), min(cols), max(cols))

main()
            
        
