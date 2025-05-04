import plotly.graph_objects as go
import numpy as np

#L1正則化とL2正則化の表示切り替えが可能なPlotlyグラフの表示
def plot_regularization(mode):
    #表示するデータの作成
    #今回は変数が2つの二次元モデルと仮定し、重みw1 w2に対しての損失関数の値を3次元プロットする
    xx = np.linspace(-20, 20, 100)
    yy = np.linspace(-20, 20, 100)
    xs,ys = np.meshgrid(xx,yy)
    z1 = 10*(xs + 12)**2 + (10/4)*(ys + 12)**2 + 100# Lossの例

    #modeによって切り替えを行う
    if mode=="L1":
        z2 = 100*(np.abs(xs) + np.abs(ys)) #L1 正則化項

    else:
        z2 = 10*(xs**2 + ys**2) #L2 正則化項

    z3 = z1+z2

    # 表示
    sur1 = go.Surface(
        #特定の範囲に等高線を描く
        contours = {
        "z": {"show": True, "start": 0, "end": 60000, "size": 500,"project":{"z":True} ,"color":"blue"}
        },
        showscale=True,
        x = xs,
        y = ys,
        z = z1,
        name="Loss",
        showlegend=True,
        type='surface',
        cauto=False,
        reversescale=False, colorbar=go.ColorBar(x=-0.84)
    )

    sur2 = go.Surface(
        contours= {
        "z":{"show":True,"start":0, "end":60000, "size":500, "project":{"z":True},"color":"red"}
        },
        showscale=True,
        x = xs,
        y = ys,
        z = z2,
        name=mode,
        showlegend=True,
        type="surface",
        cauto=False,
        reversescale=False, colorbar=go.ColorBar(x=-0.84)
    )

    sur3 = go.Surface(
        contours= {
        "z":{"show":True,"start":0, "end":60000, "size":500,"project":{"z":True}, "color":"black"}
        },
        showscale=True,
        x = xs,
        y = ys,
        z = z3,
        name="Loss+" + mode,
        showlegend=True,
        type="surface",
        cauto=False,
        reversescale=False, colorbar=go.ColorBar(x=-0.84)
    )

    fig = go.Figure()

    fig.add_trace(go.Surface(sur1))
    fig.add_trace(go.Surface(sur2))
    fig.add_trace(go.Surface(sur3))

    #最初に表示する視点や大きさを決める
    fig.update_layout(
            scene = {
                "xaxis": {"nticks": 20,"title":"w1"},
                "yaxis":{"title":"w2"},
                "zaxis": {"nticks": 4,"title":"Loss"},
                'camera_eye': {"x": 1, "y": -1.5, "z": 1},
                "aspectratio": {"x": 1, "y": 1, "z": 1}
            },
            width=700,
            height=500)

    print(fig.to_html())

###########################
#main script
#modeで切り替えを行ってください
mode = "L1"
###########################
plot_regularization(mode)
