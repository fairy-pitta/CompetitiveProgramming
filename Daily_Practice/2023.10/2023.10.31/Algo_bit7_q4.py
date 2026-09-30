
def main():
    A, M = map(int, input().split())
    if (A&M) > 0:
        print("Yes")
    else:
        print("No")

main()