def main():
    N, M = map(int, input().split())
    roads = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, input().split())
        roads[a-1].append(b-1)
        roads[b-1].append(a-1)
    for city in range(N):
        print(len(roads[city]))

main()