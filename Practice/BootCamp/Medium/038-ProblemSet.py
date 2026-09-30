from sortedcontainers import SortedSet, SortedList, SortedDict

def main():
    N = int(input())
    D = list(map(int, input().split()))
    M = int(input())
    T = list(map(int, input().split()))

    S = SortedList(D)

    for i in range(M):
        if T[i] in S:
            S.discard(T[i])
        else:
            print("NO")
            return False
    
    print("YES")
    return 

    