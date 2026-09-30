x = str(input())
n = int(input())

n = n % len(x)
print(x[n-1])