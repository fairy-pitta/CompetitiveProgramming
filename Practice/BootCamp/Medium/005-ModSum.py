def greedy(n):
    from itertools import permutations 
    seq = list(range(1,n+1))
    perm_list = list(permutations(seq))
    
    ans = 0
    ans_seq = seq
    for s in perm_list:
        temp_ans = 0
        for i in range(len(s)):
            temp_ans += seq[i]%s[i]
        
        if temp_ans > ans:
            ans_seq = s
            ans = temp_ans
        else:
            continue
    
    print(ans)
    print(ans_seq)



def main():
    N = int(input())
    print((N)*(N-1)//2)

main()