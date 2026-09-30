# 10進法をn進法に変換する
def base10to(n, b):
    if n // b:
        return base10to(n // b, b) + str(n % b)
    return str(n % b)

def main():
    N, K = map(int, input().split())
    num = str(N)
    for  i in range(K):
        base_10 = int(num, 8)
        base_9 = base10to(base_10, 9)
        num = ""
        for j in range(len(base_9)):
            if base_9[j] == "8":
                num += "5"
            else:
                num += base_9[j]
    
    return num 

print(main())
