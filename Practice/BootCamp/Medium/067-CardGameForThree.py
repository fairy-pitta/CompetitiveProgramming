from collections import deque

def main():
    A = deque(list(input()))
    B = deque(list(input()))
    C = deque(list(input()))

    winner = ""
    next = "a"

    while True:

        if next == "a":
            if len(A) == 0:
                winner = "A"
                break 
            next = A.popleft()

        elif next == "b":
            if len(B) == 0:
                winner = "B"
                break 
            next = B.popleft()

        else:
            if len(C) == 0:
                winner = "C"
                break 
            next = C.popleft()

    print(winner)

main()
            

