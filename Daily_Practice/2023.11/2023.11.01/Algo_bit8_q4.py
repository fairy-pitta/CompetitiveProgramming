
def main():
    X = list(input())
    P, Q = map(str, input().split())

    user = 0
    action = 0

    if P == "g": user = 1
    elif P == "u": user = 2

    if Q == "r": action = 2
    elif Q == "w": action = 1

    if int(X[user]) & (1<<action) > 0:
        print("Yes")
    else: 
        print("No")

main()
