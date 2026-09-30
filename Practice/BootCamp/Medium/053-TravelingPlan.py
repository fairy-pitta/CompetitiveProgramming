def main():
    N = int(input())
    A = list(map(int, input().split()))
    # 出発地点を追加
    A.insert(0,0)
    # 最終地点を追加
    A.append(0)

    total_dist = 0
    for j in range(1, len(A)):
        total_dist += abs(A[j]-A[j-1])
    
    for i in range(1, len(A)-1):
        prev = A[i-1]
        cur = A[i]
        nex = A[i+1]
        ans = total_dist - abs(cur-prev) - abs(nex-cur)
        ans += abs(nex-prev)
        print(ans)
            

main()


