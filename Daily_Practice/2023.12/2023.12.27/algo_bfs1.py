from collections import deque

def main():
    N, M = map(int, input().split())
    G = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    
    seen = set()
    seen.add(0)  # Start from vertex 0

    stack = deque([0])  # Using a deque as a queue for BFS

    print(0)
    while stack:
        v = stack.popleft()
        colored = []

        for next_v in G[v]:
            if next_v in seen:
                continue

            colored.append(next_v)
            stack.append(next_v)
            seen.add(next_v)  # Mark as seen when enqueued

        print(*colored)  # Print all newly discovered vertices at this level

main()
