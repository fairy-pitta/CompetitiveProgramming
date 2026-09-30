
def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    index_A = [[i, v] for i, v in enumerate(A)]
    sorted_index_A = sorted(index_A, key=lambda x: x[1], reverse=True)
    S = []
    P = []
    points = 0
    for i in range(N):
        s = list(input())
        player_point = i+1
        for j in range(M):
            if s[j] == "o": 
                player_point += A[j]
        S.append(s)
        P.append(player_point)
        points = max(points, player_point)

    

    for player in range(N):
        current_point = P[player]
        num = 0
        diff = abs(points-current_point)
        
        for k in range(M):
            if diff == 0:
                print(0)
                break
            if S[player][sorted_index_A[k][0]] == "x":
                diff -= sorted_index_A[k][1]
                num += 1
                if diff <= 0:
                    print(num)
                    break 
                else: 
                    continue 
main()







