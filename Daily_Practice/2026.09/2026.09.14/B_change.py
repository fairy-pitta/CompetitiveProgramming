def main():
      T = int(input())

      def solve(N):
          import math
          sq = math.isqrt(N)

          rem = N - sq ** 2

          if rem == 0:                          # 平方数ちょうど
              ans = (sq - 1) * sq * 2
          elif rem == 1:                        # +1
              ans = (sq - 1) * sq * 2 + 1
          elif rem <= sq:                       # 1列目：ここから2ずつ (rem=2..k)
              ans = (sq - 1) * sq * 2 + 1 + (rem - 1) * 2
          elif rem == sq + 1:                   # 2列目の最初（折り返し）：+1しか増えない
              ans = (sq - 1) * sq * 2 + 1 + (sq - 1) * 2 + 1
          else:                                 # 2列目：ここから2ずつ (rem=k+2..2k)
              ans = (sq - 1) * sq * 2 + 1 + (sq - 1) * 2 + 1 + (rem - sq - 1) * 2

          return ans

      for _ in range(T):
          N = int(input())
          print(solve(N))

main()