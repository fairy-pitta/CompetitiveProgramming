def main():
    N = int(input())
    T = list(map(int, input().split()))
    M = int(input())
    save = 10**18
    for _ in range(M):
        p, x = map(int, input().split())
        print(sum(T)-(T[p-1]-x))

main()