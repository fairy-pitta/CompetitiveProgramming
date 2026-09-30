
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 


def main():
    N, M = is_map(int)
    S = []
    for _ in range(N):
        s = list(input())
        S.append(s)
    
    for row in range(N-8):
        for col in range(M-8):
            if (S[row][col] == "#" and\
                S[row+1][col] == "#" and\
                S[row+2][col] == "#" and\
                S[row+1][col+1] == "#" and\
                S[row+2][col+1] == "#" and\
                S[row][col+1] == "#" and\
                S[row+2][col+2] == "#" and\
                S[row+1][col+2] == "#" and\
                S[row][col+2] == "#" and\
                S[row+3][col] == "." and\
                S[row+3][col+1] == "." and\
                S[row+3][col+2] == "." and\
                S[row+3][col+3] == "." and\
                S[row+2][col+3] == "." and\
                S[row+1][col+3] == "." and\
                S[row][col+3] == "." and\
                S[row+5][col+5] == "." and\
                S[row+6][col+5] == "." and\
                S[row+7][col+5] == "." and\
                S[row+8][col+5] == "." and\
                S[row+5][col+6] == "." and\
                S[row+5][col+7] == "." and\
                S[row+5][col+8] == "." and\
                S[row+6][col+6] == "#" and\
                S[row+6][col+7] == "#" and\
                S[row+6][col+8] == "#" and\
                S[row+7][col+6] == "#" and\
                S[row+7][col+7] == "#" and\
                S[row+8][col+8] == "#" and\
                S[row+8][col+6] == "#" and\
                S[row+8][col+7] == "#" and\
                S[row+8][col+8] == "#"):
                print(row+1, col+1)

main()
        