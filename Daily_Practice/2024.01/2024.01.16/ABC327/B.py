def main():
    B = int(input())
    for i in range(1, 10**3):
        if i ** i == B:
            print(i)
            return
    
    print(-1)

main()
