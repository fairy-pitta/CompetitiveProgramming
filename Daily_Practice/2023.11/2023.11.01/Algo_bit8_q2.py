display_list = [
    "1110111", "0100100", "1011101", "1101101", "0101110",
    "1101011", "1111011", "0100111", "1111111", "1101111"
]

def main():
    N, M = map(int, input().split())
    int_n = int(display_list[N], base = 2)
    int_m = int(display_list[M], base = 2)
    print(int_n^int_m)

main()