def main():
    N = int(input())
    first_row = list(map(int, input().split()))
    second_row = list(map(int, input().split()))

    for i in range(1, N):
        first_row[i] += first_row[i-1]
        second_row[i] += second_row[i-1]
    
    first_row.insert(0,0)
    second_row.insert(0,0)
    ans = 0

    for col in range(1, N+1):
        candies = first_row[col] + second_row[-1] - second_row[col-1]
        ans = max(ans, candies)
    
    print(ans)

main()