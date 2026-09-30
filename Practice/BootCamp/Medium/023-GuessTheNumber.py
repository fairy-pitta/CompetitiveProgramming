
def main():
    N, M = map(int, input().split())
    S = [list(map(int, input().split())) for _ in range(M)]
    start_N = [0, 10, 100]

    for i in range(start_N[N-1], 10**N):
        num = list(str(i))
        flag = True
        for j in range(M):
            s, c = S[j][0], S[j][1]
            if num[s-1] != str(c):
                flag = False
                break
        if flag:
            print(i)
            return
    
    print(-1)
    return

main()
# def main():
#     N, M = map(int, input().split())
#     num = [(-1) for _ in range(N)]
#     for _ in range(M):
#         s, c = map(int, input().split())
#         if num[s-1] == -1 or num[s-1] == c:
#             num[s-1] = c
#         else:
#             print(-1)
#             return 
    
#     if N == 1 and num[0] == 0:
#         print(0)
#         return 
    
#     for i in range(N):
#         if i == 0:
#             if num[0] == -1:
#                 num[0] = 1
#             elif num[0] == 0:
#                 print(-1)
#                 return
#         else:
#             if num[i] == -1:
#                 num[i] = 0
    
#     print("".join([str(z) for z in num]))
#     return 

# main()
            
        
