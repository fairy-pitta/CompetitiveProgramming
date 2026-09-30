
def main():
    N = int(input())
    group = []
    for i in range(10):
        if N & (1<<i):
            group.append(i)
    print(group)

main()
