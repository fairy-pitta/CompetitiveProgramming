from math import ceil

def main():
    N = int(input())
    T = [int(input()) for _ in range(5)]
    cnt = 4 + ceil(N/min(T))
    print(cnt)

main()