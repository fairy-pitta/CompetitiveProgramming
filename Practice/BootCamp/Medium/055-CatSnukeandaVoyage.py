def main():
    N, M = map(int, input().split())
    graph = [set() for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    for i in graph[1]:
        if N in graph[i]:
            print("POSSIBLE")
            return
    
    print("IMPOSSIBLE")
    return

main()
