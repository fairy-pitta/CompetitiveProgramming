"""next_permutation: リストを辞書順で「次の並び」に in-place で進める (C++ の std::next_permutation)。

    a = sorted("aab")            # ['a', 'a', 'b']  必ずソートしてから始める
    while True:
        print("".join(a))        # aab -> aba -> baa
        if not next_permutation(a):
            break

引数:
    a : 並べ替えるリスト (文字でも数でもよい)。この関数が直接書き換える
戻り値:
    次の並びに進めたら True。a が最後の並び (降順) だったら False (a は変えない)

使い分け:
    - itertools.permutations との違い: 同じ文字があっても同じ並びを 2 回出さない。
        permutations("aab") は 6 個 (aab が 2 回など)、next_permutation は aab, aba, baa の 3 個だけ
      → 「区別できる並べ方」を数える問題 (ABC363C など) ではこちら
    - 全部違う要素なら permutations で十分 (書くのが楽)
    - 「選ぶ」だけなら itertools.combinations。順番を変えて並べるのがこの関数

仕組み (例: 1 3 5 4 2 -> 1 4 2 3 5):
    1. 右から見て初めて a[i] < a[i+1] になる i を探す (3)。右側 5 4 2 は降順でもう最大なので、
       次に大きくするには a[i] を変えるしかない。見つからなければ全体が降順 = 最後の並び
    2. 右側から a[i] より大きい中で一番小さい a[j] (4) を探して入れ替える -> 1 4 5 3 2
    3. i より右 (5 3 2、まだ降順) を反転して一番小さい並びにする -> 1 4 2 3 5
    比較が >= / <= (等号つき) なので同じ値同士は入れ替えず、重複した並びが出ない。

計算量: 1 回 O(N)。全列挙は O(N! * N) (重複があればその分少ない)。N <= 10 くらいまで。

注意:
    - 最初に sorted しておかないと、その並びより辞書順で前のものが列挙されない
    - N = 10 で 10! ≈ 360 万通り。CPython だと TLE しやすいので PyPy で出す
"""

def next_permutation(a):
    n = len(a)
    # 右から見て初めて a[i] < a[i+1] となる i を探す
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i < 0:
        return False
    # 右から見て初めて a[i] < a[j] となる j と入れ替える
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    # i より右を反転して最小にする
    a[i + 1:] = a[i + 1:][::-1]
    return True
