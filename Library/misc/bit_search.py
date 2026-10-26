# bit全探索 (product で True/False の直積を回す) の実装例
# 題材: ABC249C https://atcoder.jp/contests/abc249/tasks/abc249_c
#
# ライブラリ関数ではなく、解答 1 本をそのまま置いた「書き方の見本」。
# 貼ると最後の print(solve()) で入力を読みにいくので、型だけ真似して使う。
#
# bit全探索とは:
#     N 個のものそれぞれを「使う / 使わない」で選ぶ 2^N 通りを全部試す方法。N <= 20 くらいまで。
#     product((True, False), repeat=N) は長さ N の True/False の組を 2^N 通りすべて出す。
#         product((True, False), repeat=2) -> (T, T), (T, F), (F, T), (F, F)
#     pro[i] が True なら「i 番目を選ぶ」と読む。
#     ビット演算で書くなら for mask in range(1 << N): で、(mask >> i) & 1 が pro[i] に当たる。
#
# この問題: N 個の文字列から好きなだけ選び、「選んだ文字列のうちちょうど K 個に現れる文字」の
#     種類数を最大化する。選び方 2^N 通りごとに数えて最大をとる。
#     (S[i] は各文字が高々 1 回の文字列なので、Counter で数えた値が「現れた文字列の数」になる)
#
# 計算量: O(2^N * N * |S|)。

from collections import Counter
from itertools import product 

def solve():

    N, K = map(int, input().split())
    S = []
    for _ in range(N):
        s = input()
        S.append(s)
    
    def judge(pro):
        # sub-class of dict 
        C = Counter()
        # for the list of booleans 
        for i in range(N):
            # if True 
            if pro[i]:
                # count the elements in S[i]
                # and update the counter 
                C.update(S[i])
        # how many letters appears K times 
        letters = 0
        # the items() pops the ch 'a' and cnt '9' 
        for ch, cnt in C.items():
            if cnt == K:
                letters += 1

        return letters 
    
    # worse comes worse 
    # can choose 0 
    ans = 0

    for pro in product((True, False), repeat = N):
        # if > 0 then update first 
        # afterwards compete 
        ans = max(ans, judge(pro))
    
    return ans 

print(solve())
