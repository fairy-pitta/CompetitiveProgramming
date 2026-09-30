# 1011111
# 2100010
# 3101110
# 5011111
# 6101010
# 7001111
# 8111110
# 9011111
# 10101110
# 11011010
# 12110010
# 13112010
# 14011011
# 15011010
# 16011001
# 17110110
# 18011111
# 19100010
# 21102010
# 22111010
# 23011111
# 24101010
# 25011011
# 29013010
# 30102010
# 31110010


import heapq

class PriorityQueue:
    def __init__(self):
        self._container = []

    def push(self, x):
        heapq.heappush(self._container, x)

    def pop(self):
        return heapq.heappop(self._container)

    def __len__(self):
        return len(self._container)


from collections import deque
def main():
    N = 31 
    S = []
    traits = []
    for _ in range(N):
        s = list(input())
        traits.append(s[1:])
        S.append(s)
    print(S)
    print(traits)
    tanks = [set() for _ in range(N)]
    for i in range(N):
        yet = PriorityQueue()
        for j in range(N):
            if traits[i] not in tanks[j]:
                yet.push((len(tanks[j], j)))
        
        _, num = yet.pop()
        tanks[num].add(traits[i])
    
    for i in range(N):
        if len(tanks[i]) != 0:
            print(S[i][0])
    
    return 

main()
            
            


    
