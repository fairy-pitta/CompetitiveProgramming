def main():
    S = input()

    more_than_count = [(0) for _ in range(len(S)+1)]
    less_than_count = [(0) for _ in range(len(S)+1)]

    for i in range(len(S)):
        if S[i] == "<":
            more_than_count[i+1] = more_than_count[i] + 1
    
    for j in reversed(range(len(S))):
        if S[j] == ">":
            less_than_count[j] = less_than_count[j+1] + 1
    
    ans = 0
    for k in range(len(S)+1):
        ans += max(more_than_count[k], less_than_count[k])
    
    print(ans)
    
main()