import heapq
Q = int(input())
queue = []
heapq.heapify(queue)

for i in range(Q):
    s = list(map(int, input().split()))
    if s[0] == 3:
        new_s = list(map(lambda x: x*(-1), queue))
        alt_s = queue
        maximum = heapq.heappop(new_s) * (-1)
        minimum = heapq.heappop(alt_s)
        print(maximum - minimum)
    elif s[0] == 1:
        heapq.heappush(queue, s[1])
    else:
        queue_list = list(queue)
        num = queue_list.count(s[1])
        num = min(num, s[2])
        for _ in range(num):
            queue_list.remove(s[1])
        heapq.heapify(queue_list)


    



