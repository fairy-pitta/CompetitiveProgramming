def main():
    N = int(input())
    h = list(map(int, input().split()))

    h.insert(0,0)
    h.append(0)

    cnt = 0
    for i in range(1, len(h)):
        cnt += abs(h[i]-h[i-1])
    
    print(cnt // 2)

main()