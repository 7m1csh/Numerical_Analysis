# スーパーコンピュータの性能推移(flops)

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

# 日本語フォントを設定
rcParams['font.family'] = 'Noto Sans CJK JP'

# スーパーコンピュータの歴史データ
data = [
    {"年代": 1976, "機種": "Cray-1", "方式": "ベクトル型", "プロセッサ数": 1, "MIPS": 160, "FLOPS(G)": 0.08, "実績": "世界初の商用ベクトルスーパーコンピュータ"},
    {"年代": 1985, "機種": "Cray-2", "方式": "ベクトル型", "プロセッサ数": 4, "MIPS": 250, "FLOPS(G)": 1.9, "実績": "液浸冷却方式を採用"},
    {"年代": 1993, "機種": "Intel Paragon", "方式": "MPP", "プロセッサ数": 4000, "MIPS": 100, "FLOPS(G)": 150, "実績": "大規模並列計算機"},
    {"年代": 1997, "機種": "ASCI Red", "方式": "MPP", "プロセッサ数": 9000, "MIPS": 200, "FLOPS(G)": 1338, "実績": "世界初のテラフロップス突破"},
    {"年代": 2002, "機種": "Earth Simulator", "方式": "ベクトル並列", "プロセッサ数": 5120, "MIPS": 8000, "FLOPS(G)": 35860, "実績": "気候シミュレーションで活躍"},
    {"年代": 2008, "機種": "Roadrunner", "方式": "ハイブリッド(CPU+GPU)", "プロセッサ数": 122400, "MIPS": None, "FLOPS(G)": 1020000, "実績": "ペタフロップスを世界初達成"},
    {"年代": 2011, "機種": "K computer", "方式": "スカラ並列", "プロセッサ数": 705024, "MIPS": None, "FLOPS(G)": 10500000, "実績": "10ペタフロップスを達成"},
    {"年代": 2020, "機種": "富岳", "方式": "スカラ並列 (ARM)", "プロセッサ数": 7630848, "MIPS": None, "FLOPS(G)": 442000000, "実績": "世界1位 (TOP500, HPCG, HPL-AI)"},
]

df = pd.DataFrame(data)

# FLOPSの推移を可視化（対数スケール）
plt.figure(figsize=(10,6))
plt.plot(df["年代"], df["FLOPS(G)"], marker="o", linestyle="-", label="FLOPS (G)")
plt.yscale("log")
plt.title("スーパーコンピュータの性能推移 (FLOPS)")
plt.xlabel("年代")
plt.ylabel("FLOPS [GigaFLOPS] (log scale)")
for i, row in df.iterrows():
    plt.text(row["年代"], row["FLOPS(G)"], row["機種"], fontsize=8, ha="left", va="bottom")

plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.show()

