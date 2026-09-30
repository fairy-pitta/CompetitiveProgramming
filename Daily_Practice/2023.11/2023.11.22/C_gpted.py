def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def lehmer_to_permutation(N, lehmer):
    permutation = []
    elements = list(range(1, N + 1))

    for code in lehmer:
        permutation.append(elements.pop(code))

    return permutation

def find_previous_permutation(N, P):
    lehmer = [0] * N

    for i in range(N):
        count = 0
        for j in range(i + 1, N):
            if P[j] < P[i]:
                count += 1

        lehmer[i] = count

    return lehmer_to_permutation(N, lehmer)

def main():
    N = int(input())
    P = list(map(int, input().split()))

    previous_permutation = find_previous_permutation(N, P)
    print(*previous_permutation)

main()
