# Practice 15.2 アムダールの法則とグスタフソンの法則

import numpy as np
import matplotlib.pyplot as plt

# 並列化率 P（例: 95%）
P = 0.95

# プロセッサ数の範囲
N = np.arange(1, 65)

# アムダールの法則
amdahl_speedup = 1 / ((1 - P) + P / N)

# グスタフソンの法則
gustafson_speedup = N - (1 - P) * (N - 1)

# プロット
plt.figure(figsize=(8, 5))
plt.plot(N, amdahl_speedup, label="Amdahl's Law", color='blue', linewidth=2)
plt.plot(N, gustafson_speedup, label="Gustafson's Law", color='red', linestyle='--', linewidth=2)

# 軸ラベルとタイトル
plt.xlabel("Number of Processors (N)", fontsize=12)
plt.ylabel("Speedup", fontsize=12)
plt.title(f"Speedup Comparison (Parallel fraction P={P})", fontsize=14)

# グリッド・凡例
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()

plt.show()

