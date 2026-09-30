N, M = map(int, input().split())
S = input()
T = input()

ans = 3

if S == T[:len(S)] == T[len(T)-len(S):]: ans = 0
elif S == T[:len(S)]: ans = 1
elif S == T[len(T)-len(S):]: ans = 2

print(ans)
