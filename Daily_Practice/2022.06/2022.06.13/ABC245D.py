import numpy as np
n,m = map(int,input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

a_poly = np.poly1d(A)
c_poly = np.poly1d(C)

b_poly = c_poly / a_poly

ans = []
for i in reversed(range(m+1)):
  ans.append(int(b_poly[0][i]))
print(*ans)