def main():
    N, M = map(int, input().split())
    from collections import defaultdict 
    d = defaultdict(int)
    check = {}
    for _ in range(M):
        s, c = map(int, input().split())
        
        