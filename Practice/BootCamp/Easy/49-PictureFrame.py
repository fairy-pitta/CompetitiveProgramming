
def main():
    H, W = map(int, input().split())
    ans = []
    ans.append("#" for _ in range(W+2))
    for _ in range(H):
        a = list(input())
        a.insert(0, "#")
        a.append("#")
        ans.append(a)
    ans.append("#" for _ in range(W+2))

    for i in range(len(ans)):
        to_print = "".join(ans[i])
        print(to_print)

main()

