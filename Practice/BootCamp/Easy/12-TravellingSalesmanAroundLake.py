
def main():
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    dist = []
    for i in range(N):
        if i == 0:
            dist.append(A[i]+(K-A[-1]))
        else:
            dist.append(A[i]-A[i-1])
    print(K-max(dist))

main()