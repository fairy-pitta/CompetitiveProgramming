
# This is a template to use on solving problems 

## inputs 
def is_int(): return int(input())
def is_map(type): return map(type, input().split())
def to_list(): return [int(i) for i in list(input())]

## frequently used functions 
from math import sqrt, ceil, floor 



def main():
    N, K = is_map(int)
    scores = []
    score_sums = []
    for _ in range(N):
        s = list(is_map(int))
        scores.append(s)
        score_sums.append(sum(s))
    
    score_sums_sorted = sorted(score_sums, reverse = True)

    for i in range(N):
        final_score = score_sums[i] + 300
        if final_score >= score_sums_sorted[K-1]:
            print("Yes")
        else:
            print("No")


main()