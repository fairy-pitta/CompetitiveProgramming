def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    S = [0] * (N + 1)
    for i in range(N):
        S[i + 1] = S[i] + A[i]

    exist = set(S) 
    for i in S:
        if (i + P) in exist and (i + P + Q) in exist and (i + P + Q + R) in exist:
            return True
    return False


if main(): print("Yes")
else: print("No")