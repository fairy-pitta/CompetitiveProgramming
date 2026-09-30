def main():
    A, M = map(int, input().split())
    print((A&M)^(A|M))

main()