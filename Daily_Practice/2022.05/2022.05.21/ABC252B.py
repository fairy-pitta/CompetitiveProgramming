def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    max_A = max(A)
    a_indices = set()
    for i in range(N):
        if A[i] == max_A:
            a_indices.add(i+1)
    for dislike in B:
        if dislike in a_indices:
            return "Yes"
            break 
    #print(a_indices)
    return "No"

print(main())