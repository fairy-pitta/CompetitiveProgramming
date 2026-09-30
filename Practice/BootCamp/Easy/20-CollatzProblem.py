
def main():
    s = int(input())
    numbers = set()
    numbers.add(s)
    cnt = 1
    n = s
    while True:

        if n%2: n=3*n+1
        else: n//=2
        cnt += 1
        if n in numbers:
            break 
        else:
            numbers.add(n)
    
    print(cnt)

main()
