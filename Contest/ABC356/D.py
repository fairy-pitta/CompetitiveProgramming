def solve(N, M):
    MOD = 998244353
    total_popcount = 0
    
    for i in range(64):  
        if M & (1 << i):
            count_ones = 0
            cycle_length = 1 << (i + 1)
            full_cycles = N // cycle_length
            count_ones += (full_cycles * (cycle_length // 2))
            remaining = N % cycle_length
            count_ones += max(0, (remaining + 1) - (cycle_length // 2))
            
            total_popcount += count_ones
    
    return total_popcount % MOD

N, M = map(int, input().split())
print(solve(N, M))
