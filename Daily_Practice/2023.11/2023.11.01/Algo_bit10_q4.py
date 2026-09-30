
def main():
    N = int(input())
    W = list(map(str, input().split()))

    ans = 10**7

    for i in range(2**N):
        alphabet_set = set()
        num = 0
        for j in range(N):
            if i&(1<<j) > 0:
                for letter in W[j]:
                    alphabet_set.add(letter)
                num += 1
        if len(alphabet_set) == 26:
            ans = min(ans, num)
    
    if ans < 10**7:
        print(ans)
    else:
        print(-1)

main()