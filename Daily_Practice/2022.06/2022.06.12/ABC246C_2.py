N, K, X = map(int, input().split())
A = list(map(ijnt, input().split()))

# how much it costs right now 
ans = sum(A)
# how many coupons we have left 
rem = K

# how many times can we minus X?
Q = sum(x // X for x in A)

R = sorted((x % X for x in A), reverse=True)  # X円引きし終わったあとの余りを大きい順に並べる
ans -= X * min(Q, rem)  # Qとクーポンの枚数の少ない方だけX円引きできる
rem -= min(Q, rem)  # X円引きに使った分クーポンを減らす
ans -= sum(R[:rem])  # 大きい順に使う（スライスは配列外参照を起こさないので、remが巨大でも問題ありません）
print(ans)