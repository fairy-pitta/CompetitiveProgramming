from collections import deque

def main():
    X = list(input())
    stack = deque([])
    for i in range(len(X)):
        stack.append(X[i])
        if len(stack) > 1 and stack[-1] == "T" and stack[-2] == "S":
            stack.pop()
            stack.pop()
    
    print(len(stack))

main()
