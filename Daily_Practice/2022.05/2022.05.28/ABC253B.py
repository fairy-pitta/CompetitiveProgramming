from colorsys import ONE_SIXTH


def main():
    H, W = map(int, input().split())
    one_x = -1
    one_y = -1
    two_x = -1
    two_y  = -1
    for i in range(H):
        s = list(input())
        for j in range(W):
            if s[j] == "o":
                if one_x == -1:
                    one_x = i
                    one_y = j
                else:
                    two_x = i
                    two_y = j
                    break 
    ans = abs(one_x - two_x) + abs(one_y - two_y)
    return ans 

print(main())


