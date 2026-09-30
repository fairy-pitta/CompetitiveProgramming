m = int(input())

vv = 0

if m < 100:
    vv = str("00")
elif m <= 5000:
    vv = m*10//1000
    vv = str(vv).zfill(2)
elif m <= 30000:
    vv = m // 1000 + 50
elif m <= 70000:
    vv = (m // 1000 - 30) // 5 + 80
else:
    vv = 89

print(vv)