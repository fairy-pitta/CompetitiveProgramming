from collections import Counter
from itertools import product 

def solve():

    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    
    def judge(pro):
        # sub-class of dict 
        C = Counter()
        # for the list of booleans 
        for i in range(N):
            # if True 
            if pro[i]:
                # count the elements in S[i]
                # and update the counter 
                C.update(S[i])
        # how many letters appears K times 
        letters = 0
        # the items() pops the ch 'a' and cnt '9' 
        for ch, cnt in C.items():
            if cnt == K:
                letters += 1

        return letters 
    
    # worse comes worse 
    # can choose 0 
    ans = 0

    for pro in product((True, False), repeat = N):
        # if >0 then update first 
        # afterwards compete 
        ans = max(ans, judge(pro))
    
    return ans 

print(solve())
