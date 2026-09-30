def main():
    N, M = map(int, input().split())
    # N : how many sang 
    # M : how long the song is 
    A = []
    # the song 
    for _ in range(M):
        a = int(input())
        A.append(a)
    Scores = -1000
    for person in range(N):
        well = []
        for r in range(M):
            h = int(input())
            well.append(h)
        score = 100
        for diff in range(M):
            if abs(A[diff] - well[diff]) > 30:
                score -= 5
            elif abs(A[diff] - well[diff]) > 20:
                score -= 3
            elif abs(A[diff] - well[diff]) > 10:
                 score -= 2
            elif abs(A[diff] - well[diff]) > 5:
                score -= 1
            else:
                continue 
        if score <= 0:
            score = 0
        Scores = max(Scores, score)
    return Scores 

print(main())

            

