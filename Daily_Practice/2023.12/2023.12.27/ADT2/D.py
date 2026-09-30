letters = ["A", "B", "C", "D", "E", "F", "G"]
dist = [0, 3, 4,8,9,14,23]
p,q = map(str, input().split())
a = letters.index(p)
b = letters.index(q)
print(dist[max(a,b)]-dist[min(a,b)])
