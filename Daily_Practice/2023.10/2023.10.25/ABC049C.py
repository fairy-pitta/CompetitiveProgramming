S = input()
S = S.replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")
if S == "":
  print("YES")
else:
  print("NO")