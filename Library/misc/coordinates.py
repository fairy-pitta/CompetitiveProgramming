"""点の回転: 点 (x, y) を中心 (p, q) のまわりに theta ラジアン回転した座標を返す。

    anti_clockwise(1, 0, 0, 0, pi / 2)  ->  (約 0.0, 1.0)   # 反時計回りに 90 度
    clockwise(1, 0, 0, 0, pi / 2)       ->  (約 0.0, -1.0)  # 時計回りに 90 度

度で与えられたら math.radians(deg) でラジアンにする。

仕組み:
    中心を原点に平行移動してから、回転行列
        [cos θ  -sin θ]
        [sin θ   cos θ]
    を掛け、元の位置に戻す。時計回りは「反時計回りに 2π - θ」と同じ。

注意: 結果は float。cos(pi / 2) は 0 ではなく 6e-17 のような値になるので、
      整数の答えがほしいなら round し、比較するなら誤差 (1e-9 など) を許すこと。
計算量: O(1)。
"""
from math import pi, cos, sin

# (x,y) を(p, q)を中心に反時計回りに theta(radian) 回転させる
def anti_clockwise(x, y, p, q, theta):
    new_x = (x - p) * cos(theta) - (y - q) * sin(theta) + p
    new_y = (x - p) * sin(theta) + (y - q) * cos(theta) + q
    return (new_x, new_y)


# (x,y) を(p, q)を中心に時計回りに theta(radian) 回転させる
def clockwise(x, y, p, q, theta):
    new_theta = 2 * pi - theta
    return anti_clockwise(x, y, p, q, new_theta)