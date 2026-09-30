from math import lcm

def check(N, M, K, num):
    cnt = num // N + num // M - 2 * (num // lcm(N, M))
    if cnt >= K:
        return True
    return False

N, M, K = map(int, input().split())

def meguru_bisect(l, r):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    l r は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(r - l) > 1):
        mid = (r + l) // 2
        if check(N, M, K, mid):
            r = mid
        else:
            l = mid
    return r



print(meguru_bisect(0, 10**18))