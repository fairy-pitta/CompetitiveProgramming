N = int(input())

from sortedcontainers import SortedList 
from operator import itemgetter
cards = []
ans = []
strength = SortedList([])
cost = SortedList([])

for i in range(N):
    a, c = map(int, input().split())
    cards.append([a,c,i])
    cost.append(c)

sortedbystrength = sorted(cards)
sortedbycost = sorted(cards, key=itemgetter(1))

for j in range(N):
    num = sortedbystrength[1]
    idx = cost.index(num)
    if idx == 0:
        ans.append(cards[2])
    else:
        min_idx = 

