from collections import defaultdict, deque

def shift_list_one_right(deque_list):
    deque_list.rotate(1)
    return deque_list

def main():
    N, M = map(int, input().split())
    S = list(input())
    C = list(map(int, input().split()))

    # Create a dictionary to store positions of each color in the string
    color_positions = defaultdict(deque)
    for i in range(N):
        color_positions[C[i]].append(i)

    # Perform right circular shift for each color
    for color in range(1, M + 1):
        positions = color_positions[color]
        positions = shift_list_one_right(positions)
        color_positions[color] = positions

    # Construct the final string based on the color positions
    ans = [""] * N
    for color in range(1, M + 1):
        positions = color_positions[color]
        for i, pos in enumerate(positions):
            ans[pos] = S[positions[i - 1]]

    final_string = "".join(ans)
    print(final_string)

main()
