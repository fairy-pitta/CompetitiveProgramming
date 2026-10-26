"""最小公倍数 (LCM): x と y の両方で割り切れる最小の正の整数。

    my_lcm(4, 6)  ->  12

仕組み: x * y = gcd(x, y) * lcm(x, y) が成り立つので、lcm = x * y // gcd。
3 つ以上なら reduce(my_lcm, A) で畳み込む。
Python 3.9 以降は標準の math.lcm(*A) でも同じことができる。
template.py にも同じ my_lcm が入っている。

計算量: O(log min(x, y))（gcd の分）。
"""
import math

def my_lcm(x, y):
    return (x * y) // math.gcd(x, y)