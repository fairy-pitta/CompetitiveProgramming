def main():
    W, H, x, y = map(int, input().split())

    if x*2 == W and y*2 == H:
        print(H*W/2, 1)
    else:
        print(H*W/2, 0)

main()