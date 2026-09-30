def main():
    N, K, Q = map(int, input().split())
    players_point = [(K) for _ in range(N)]
    for _ in range(Q):
        a = int(input())
        players_point[a-1] += 1
    
    for player in range(N):
        if players_point[player] <= Q:
            print("No")
        else:
            print("Yes")
    
main()

