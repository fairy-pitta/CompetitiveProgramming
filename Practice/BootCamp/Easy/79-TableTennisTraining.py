def main():
    N, A, B = map(int, input().split())
    
    if abs(A-B)%2==0:
        return abs(A-B)//2
    
    dist_to_top = (A+B) // 2
    dist_to_bottom = ((N-B)+(N-A)) // 2 + 1

    return min(dist_to_top, dist_to_bottom)

print(main())