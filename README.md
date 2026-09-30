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

| | 内容 |
|---|---|
| `numeric/` | `lcm` `cmb` `divisors` `factorize` `primes` `modint` `notation` |
| `graph/` | `bfs_2d` `dijkstra` `dijkstra_max_jump` `unionfind` `tree_diameter` `bipartite` `build_graph` |
| `structure/` | `segtree` `sorted_set` `multiset` `priority_queue` |
| `misc/` | `meguru_bisect` `coordinates` `iscolinear` `bit_search` |

ディレクトリ名に `math` を使うと Python の名前空間パッケージが標準ライブラリの
`math` を隠すため `numeric` としている。`misc/meguru_bisect.py` も同じ理由で
`bisect.py` を避けている。
