
def main():
    N = int(input())
    a = list(map(int, input().split()))
    a = sorted(a, reverse = True)

    num_teams = 0
    strength = 0

    for player in range(3*N):
        if num_teams < N:
            if player%2:
                num_teams += 1
                strength += a[player]
            else:
                continue
        else:
            break 

    print(strength)

main()

