def main():
      N, A, B, C, D = map(int, input().split())
      S = input()


      def no_double_rock(l, r):       
          for p in range(l, r):        
              if S[p - 1] == "#" and S[p] == "#":
                  return False
          return True

      if not (no_double_rock(A, C) and no_double_rock(B, D)):
          return False                

      if C < D:
          return True                  

      for m in range(B, D + 1):     
          if S[m - 2] == "." and S[m - 1] == "." and S[m] == ".":
              return True
      return False


print("Yes" if main() else "No")