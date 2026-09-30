from collections import defaultdict

def main():
    N, M = map(int, input().split())
    d = defaultdict(list)
    for _ in range(M):
        p, s = map(str, input().split())
        d[int(p)].append(s)
    
    AC_num = 0
    WA_num = 0

    for result in d.values():
        if "AC" in set(result):
            AC_num += 1
            for submission in result:
                if submission == "WA":
                    WA_num += 1
                else:
                    break

    print(AC_num, WA_num)

main()
