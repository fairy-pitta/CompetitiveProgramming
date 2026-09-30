from itertools import permutations 

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    li = list(permutations(range(N)))
    
    for order in li:
        flag = True
        for seq in range(1, N):
            now = S[order[seq]]
            prev = S[order[seq-1]]
            cnt = 0
            for i in range(M):
                if now[i] != prev[i]:
                    cnt += 1
            
            if cnt != 1:
                flag = False
        
        if flag:
            return True
    
    return False
            

if main():
    print("Yes")
else:
    print("No")