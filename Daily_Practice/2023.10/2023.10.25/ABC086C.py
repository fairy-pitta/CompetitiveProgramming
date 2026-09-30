N = int(input())

li = []
for _ in range(N):
  t, x, y = map(int, input().split())
  li.append([t, x, y])

ct = 0
cx = 0
cy = 0

flag = 1
for i in range(N):
  if not flag: break
  t, x, y = li[i][0], li[i][1], li[i][2]
  t_diff = abs(t-ct)
  x_dist = abs(cx-x)
  y_dist = abs(cy-y)

  ct = t
  cx = x
  cy = y

  if t_diff < x_dist + y_dist:
    flag = 0
  elif t_diff > x_dist + y_dist:
    if (x_dist + y_dist - t_diff) % 2:
      flag = 0

if flag:
  print("Yes")
else:
  print("No")
    
    
  
  
  
  