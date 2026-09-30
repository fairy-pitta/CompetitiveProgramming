def main():
    R, G, B, N = map(int, input().split())
    cnt = 0

    for red in range(3001):
        for green in range(3001):
            if N-red*R-green*G >= 0 and (N-red*R-green*G)%B == 0:
                cnt += 1
    
    print(cnt)

main()