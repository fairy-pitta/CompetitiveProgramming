
def main():
    A, i = map(int, input().split())
    print(A ^ (1<<i))

main()