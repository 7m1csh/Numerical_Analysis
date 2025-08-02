# 演習問題 13.1
"""
$f(x,y) = x^2 + 2xy + y^2$ に対して、
偏微分 $f_x, f_y, f_{xx}, f_{yy}$ を求めよ。
"""

from sympy import symbols, diff

# シンボリック変数xとyを定義
x, y = symbols('x y')

# 関数f(x,y)を定義
f = x**2 + 2*x*y + y**2

# f_x (fのxに関する1階偏微分) を計算
f_x = diff(f, x)

# f_y (fのyに関する1階偏微分) を計算
f_y = diff(f, y)

# f_xx (fのxに関する2階偏微分) を計算
f_xx = diff(f, x, 2)

# f_yy (fのyに関する2階偏微分) を計算
f_yy = diff(f, y, 2)

print(f"f(x,y) = {f}")
print(f"f_x = {f_x}")
print(f"f_y = {f_y}")
print(f"f_xx = {f_xx}")
print(f"f_yy = {f_yy}")
