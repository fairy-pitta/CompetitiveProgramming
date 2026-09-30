def main():
    N = int(input())
    T, A = map(int, input().split())
    H = list(map(int, input().split()))
    H_temp = [T-x*0.006 for x in H]
    diff = -10**18
    idx = 0
    for i in range(N):
        if abs(H_temp[i]-A) < abs(diff-A):
            diff = H_temp[i]
            idx = i
    print(idx+1)

main()