import plotly.graph_objects as go
import numpy as np

def plot_regularization(mode):
    xx = np.linspace(-20, 20, 100)
    yy = np.linspace(-20, 20, 100)
    xs, ys = np.meshgrid(xx, yy)
    z1 = 10 * (xs + 12)**2 + (10 / 4) * (ys + 12)**2 + 100

    if mode == "L1":
        z2 = 100 * (np.abs(xs) + np.abs(ys))
    else:
        z2 = 10 * (xs**2 + ys**2)

    z3 = z1 + z2

    sur1 = go.Surface(
        contours={"z": {"show": True, "start": 0, "end": 60000, "size": 500, "project": {"z": True}, "color": "blue"}},
        showscale=True,
        x=xs,
        y=ys,
        z=z1,
        name="Loss",
        showlegend=True,
        cauto=False,
        reversescale=False,
        colorbar=go.ColorBar(x=-0.84)
    )

    sur2 = go.Surface(
        contours={"z": {"show": True, "start": 0, "end": 60000, "size": 500, "project": {"z": True}, "color": "red"}},
        showscale=True,
        x=xs,
        y=ys,
        z=z2,
        name=mode,
        showlegend=True,
        cauto=False,
        reversescale=False,
        colorbar=go.ColorBar(x=-0.84)
    )

    sur3 = go.Surface(
        contours={"z": {"show": True, "start": 0, "end": 60000, "size": 500, "project": {"z": True}, "color": "black"}},
        showscale=True,
        x=xs,
        y=ys,
        z=z3,
        name="Loss+" + mode,
        showlegend=True,
        cauto=False,
        reversescale=False,
        colorbar=go.ColorBar(x=-0.84)
    )

    fig = go.Figure()

    fig.add_trace(sur1)
    fig.add_trace(sur2)
    fig.add_trace(sur3)

    fig.update_layout(
        scene={
            "xaxis": {"nticks": 20, "title": "w1"},
            "yaxis": {"title": "w2"},
            "zaxis": {"nticks": 4, "title": "Loss"},
            'camera_eye': {"x": 1, "y": -1.5, "z": 1},
            "aspectratio": {"x": 1, "y": 1, "z": 1}
        },
        width=700,
        height=500
    )

    with open("output.html", "w") as f:
        f.write(fig.to_html())

mode = "L1"
plot_regularization(mode)

