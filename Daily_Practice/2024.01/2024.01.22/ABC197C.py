N = int(input())
A = list(map(int, input().split()))

def or_of_sublists(two_dim_list):
    result = []
    for sublist in two_dim_list:
        sublist_or = 0
        for item in sublist:
            sublist_or |= item
        result.append(sublist_or)
    return result

def xor_of_list_elements(lst):
    """
    Takes a list and returns the XOR of all its elements.
    """
    result_xor = 0
    for item in lst:
        result_xor ^= item
    return result_xor

    
from itertools import product 

parts = list(product((0, 1), repeat=N-1))

ans = 10**18


for i in parts:
    tmp = list(i)
    tmp.append(1)
    # print(tmp)
    candidate = []
    li = []
    for j in range(len(tmp)):
        if tmp[j] == 0:
            li.append(A[j])
        else:
            li.append(A[j])
            candidate.append(li)
            li = []
    
    or_results = or_of_sublists(candidate)
    xor_result = xor_of_list_elements(or_results)
    ans = min(ans, xor_result)

print(ans)



