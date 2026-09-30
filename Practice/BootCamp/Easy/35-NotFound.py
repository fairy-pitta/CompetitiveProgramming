lowercase_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
                'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
                's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def main():
    S = set(list(input()))
    lowercase_list_bool = [(False) for _ in range(26)]
    for i in range(26):
        if lowercase_list[i] in S:
            lowercase_list_bool[i] = True
    ans = None
    for j in range(26):
        if not lowercase_list_bool[j]: 
            ans = lowercase_list[j]
            return ans
    
    return ans 

print(main())
