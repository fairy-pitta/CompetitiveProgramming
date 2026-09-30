from xml.etree.ElementTree import TreeBuilder


N = int(input())

trial = []

trial.append([1])
trial.append([1, 1])
trial.append([1,2,1])
trial.append([1, 3, 3, 1])
trial.append([1, 4, 6, 4, 1])
trial.append([1, 5, 10, 10, 5, 1])
trial.append([1, 6, 15, 20, 15, 6, 1])
trial.append([1, 7, 21, 35, 35, 21, 7, 1])
trial.append([1, 8, 28, 56, 70, 56, 28, 8, 1])
trial.append([1, 9, 36, 84, 126, 126, 84, 36, 9, 1])

if N <= 10:
    for i in range(N):
        a = trial[i]
        print(*a)
else:
    for i in range(10):
        a = trial[i]
        print(*a)
    for i in range(10, N):
        trial.append([1])
        for j in range(1, len(trial[i-1])):
            trial[i].append(trial[i-1][j-1] + trial[i-1][j])
        trial[i].append(1)

        print(*trial[i])

