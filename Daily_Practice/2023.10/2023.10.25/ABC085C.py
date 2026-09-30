N, Y = map(int, input().split())

def main():
  ans = [-1, -1, -1]
  for i in range(N+1):
    for j in range(N-i+1):
      if 10000 * i + 5000 * j + 1000 * (N-i-j) == Y:
        ans = [i, j, N-i-j]
        break
  
  print(*ans)

main()
      