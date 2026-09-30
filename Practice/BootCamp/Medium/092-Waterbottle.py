from math import atan, degrees

def main():
    a, b, x = map(int, input().split())
    if a**2*b == x:
        print(0)
        return
    if x > a**2*b/2:
        print(90-degrees(atan(a/(2*b-2*x/a**2))))
    else:print(90-degrees(atan(2*x/(a*(b**2)))))

main()