
def main():
    N = int(input())
    A = list(map(int, input().split()))
    odd = 0
    four = 0
    even = 0

    for i in A:
        if i % 4 == 0:
            four += 1
        elif i % 2 == 1:
            odd += 1
        else:
            even += 1
    
    if four >= odd:
        print("Yes")
    elif four == odd-1 and even == 0:
        print("Yes")
    else:
        print("No")
main()