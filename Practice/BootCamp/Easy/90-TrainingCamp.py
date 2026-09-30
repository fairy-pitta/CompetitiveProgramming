def main():
    mod = 10**9 + 7
    power = 1
    for i in range(int(input())):
        power = power * (i+1) % mod
    
    print(power)

main()

