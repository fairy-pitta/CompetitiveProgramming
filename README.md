# Competitive Programming

it is an art of thinking.

AtCoder を中心とした競技プログラミングの記録。Python 3.11。

## ディレクトリ構成

| ディレクトリ | 内容 | 規模 |
|---|---|---|
| `Contest/` | コンテスト本番の提出コード | 34コンテスト / 172ファイル |
| `Daily_Practice/` | 日々の練習ログ（日付単位） | 2022.05〜2026.09 / 160日 / 532ファイル |
| `Practice/` | 教材単位の演習 | 267ファイル |
| `Library/` | 貼り付け用スニペット | 23ファイル |
| `Archive/` | 更新の止まった置き場 | 17ファイル |

## 命名規則

| 対象 | 規則 | 例 |
|---|---|---|
| コンテスト | 大文字の略称 + 番号 | `Contest/ABC354/` |
| 月フォルダ | `YYYY.MM` | `Daily_Practice/2026.09/` |
| 日フォルダ | `YYYY.MM.DD`（月を省略しない） | `Daily_Practice/2026.09/2026.09.30/` |
| 解答（練習） | `<問題ID>.py` | `ABC354C.py` |
| 解答（コンテスト） | `<問題記号>.py` | `C.py` |

## Practice

| | 内容 |
|---|---|
| `BootCamp/` | AtCoder Boot Camp（Easy / Medium / Hard） |
| `DP/` | DP演習（I-Introduction 〜 IV-Practice、および EDPC） |
| `鉄則本/` | 競技プログラミングの鉄則（A01〜） |
| `AHC/` | AtCoder Heuristic Contest |

## Library

貼り付けて使うスニペット集。`template.py` が提出用の雛形。

各ファイルの先頭に、何をするか・使い方の例・似たファイルとの違い・仕組み・計算量・注意点を書いている。

| ファイル | 何をするか | 計算量 |
|---|---|---|
| `numeric/divisors.py` | `calc_divisors(N)`: N の約数を全部、小さい順に返す。`12 -> [1, 2, 3, 4, 6, 12]` | O(√N) |
| `numeric/factorize.py` | `factorize(N)`: 素因数分解。`[[素数, 指数], ...]` を返す。`12 -> [[2, 2], [3, 1]]` | O(√N) |
| `numeric/primes.py` | エラトステネスの篩。0〜N の素数判定表、N 以下の素数の列挙 | O(N log log N) |
| `numeric/lcm.py` | 最小公倍数 | O(log N) |
| `numeric/cmb.py` | 二項係数 nCr を多倍長整数で（mod なし。r < 0 や r > n は 0） | O(r) |
| `numeric/modint.py` | MOD で割った余りを自動で保つ整数クラス | O(1) / 割り算 O(log MOD) |
| `numeric/notation.py` | 10 進数と b 進数 (b <= 10) の変換 | O(桁数) |
| `graph/dijkstra.py` | 重み 0 以上のグラフの単一始点最短距離 | O((N+M) log N) |
| `graph/dijkstra_max_jump.py` | ダイクストラ + 最短経路のうち辺数最大のものを選び、経路復元 | O((N+M) log N) |
| `graph/bfs_2d.py` | ABC276E 専用のグリッド BFS（S を通る閉路判定） | O(HW) |
| `graph/unionfind.py` | Union-Find。グループの合体と同じグループか判定 | ほぼ O(1) |
| `graph/tree_diameter.py` | 木の直径（BFS を 2 回） | O(N) |
| `graph/bipartite.py` | 二部グラフ判定 | O(N+M) |
| `graph/build_graph.py` | グラフ入力の受け取り方のスニペット集 | - |
| `structure/segtree.py` | セグメント木。1 点更新・区間の min/max/sum など | O(log N) |
| `structure/sorted_set.py` | 重複なしのソート済み集合（「x 以上で最小」が探せる set） | O(√N) |
| `structure/multiset.py` | 重複ありのソート済み多重集合 | O(√N) |
| `structure/priority_queue.py` | heapq の薄いラッパー（最小値の取り出し） | O(log N) |
| `misc/meguru_bisect.py` | めぐる式二分探索（ng / ok の境目を探す） | O(log 範囲) |
| `misc/coordinates.py` | 点の回転 | O(1) |
| `misc/iscolinear.py` | 3 点が一直線上か（外積） | O(1) |
| `misc/bit_search.py` | bit 全探索の書き方の見本（ABC249C の解答） | O(2^N) |

迷いやすい組み合わせ:

- `divisors` と `factorize`: 約数そのものがほしいなら `calc_divisors`、素数と指数がほしいなら `factorize`
- `sorted_set` と `multiset`: 同じ値を何個も入れるなら `multiset`
- `dijkstra` と `dijkstra_max_jump`: 経路の復元や辺数が要るときだけ `dijkstra_max_jump`
- `priority_queue` と `sorted_set`: 最小値を取り出すだけなら `priority_queue`、任意の値の削除や「x 以上で最小」が要るなら `sorted_set`

### 生成 AI に関するルールへの対応

AtCoder の[生成 AI に関するルール](https://info.atcoder.jp/entry/llm-rules-ja)では、生成 AI を使って
作ったコードをコンテストで使うには、コンテスト開始前に Web 上に公開し、提出コードにその URL を
書く必要がある。GitHub のリポジトリなら、リポジトリの URL を 1 つ書けば足りる。

- このリポジトリは公開している。ライブラリの URL は
  <https://github.com/fairy-pitta/CompetitiveProgramming/tree/main/Library>
- `template.py` の 1 行目にこの URL を書いてある。練習ファイルは atcoder-vc がこのテンプレートから
  生成するので、新しいファイルには自動で入る。コンテスト用に手で作るファイルにも、この行を残す。
- ライブラリを直したら、使うコンテストの開始前に push して main に入れておく（公開時刻が残るように）。
- 外部から持ってきたコードは出典 URL をファイルに残す。`sorted_set.py` / `multiset.py` は
  tatyam さんの SortedSet（Unlicense）、`segtree.py` / `modint.py` は Qiita 記事から。

ディレクトリ名に `math` を使うと Python の名前空間パッケージが標準ライブラリの
`math` を隠すため `numeric` としている。`misc/meguru_bisect.py` も同じ理由で
`bisect.py` を避けている。
