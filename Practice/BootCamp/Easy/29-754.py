
def main():
    S = list(input())
    diff = 753
    for i in range(len(S)-2):
        num = S[i] + S[i+1] + S[i+2]
        diff = min(diff, abs(753-int(num)))
    print(diff)

main()


