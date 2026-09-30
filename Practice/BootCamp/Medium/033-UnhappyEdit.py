from collections import deque

def main():
    S = list(input())
    A = deque([])

    for i in S:
        if i == "0":
            A.append("0")
        elif i == "1":
            A.append("1")
        else:
            if len(A) > 0:
                A.pop()
            else:
                continue
    
    ans = "".join(list(A))
    print(ans)

main()