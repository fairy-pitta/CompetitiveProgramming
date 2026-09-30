import heapq
from collections import deque

def main():
    Q = int(input())
    d = deque([])
    h = []
    heapq.heapify(h)

    for _ in range(Q):
        # print(h)
        # print(d)
        q = list(map(int, input().split()))
        if q[0] == 1:
            d.append(q[1])
        elif q[0] == 2:
            if len(h) > 0:
                print(heapq.heappop(h))
            else:
                print(d.popleft())
        else:
            li = list(d)
            while d:
                heapq.heappush(h, d.popleft())

main()