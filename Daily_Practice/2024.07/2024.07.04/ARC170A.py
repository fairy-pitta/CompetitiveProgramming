N = int(input())
S = input()
T = input()

A_idx = []
B_idx = []

for i in range(N):
    if S[i] == "A" and T[i] == "B":
        B_idx.append(i)
    elif S[i] == "B" and T[i] == "A":
        A_idx.append(i)

# print(A_idx)
# print(B_idx)


def main():
    if min(A_idx) > min(B_idx):
        return -1
    elif max(A_idx) > max(B_idx):
        return -1
    elif (not len(A_idx)) or (not len(B_idx)):
        return -1
    else:
        return max(len(A_idx), len(B_idx))


print(main())
