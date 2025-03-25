#  Practice 9.3 三重対角行列の生成

import numpy as np
from scipy.sparse import diags

# 主対角成分
b = np.array([2, 2, 2, 2], dtype=float)
# 下対角成分
a = np.array([-1, -1, -1], dtype=float)
# 上対角成分
c = np.array([-1, -1, -1], dtype=float)

print("上対角成分: ", c)
print("対角成分  : ", b)
print("下対角成分: ", a)
print("")


# 三重対角行列の生成
T = diags([a, b, c], offsets=[-1, 0, 1]).toarray()

# 出力
print("生成された三重対角行列:\n",T)

