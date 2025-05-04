# L2正則化 ラムダの値の変化による最小解の変化
# https://github.com/parrt/website-explained.ai/blob/master/regularization/code/l2loss_with_penalty.py

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.patches import Circle
import mpl_toolkits.mplot3d.art3d as art3d
import glob
import os
from PIL import Image as PIL_Image

def diamond(lmbda=1, n=100):
    "get points along diamond at distance lmbda from origin"
    points = []
    x = np.linspace(0, lmbda, num=n // 4)
    points.extend(list(zip(x, -x + lmbda)))
    x = np.linspace(0, lmbda, num=n // 4)
    points.extend(list(zip(x,  x - lmbda)))
    x = np.linspace(-lmbda, 0, num=n // 4)
    points.extend(list(zip(x, -x - lmbda)))
    x = np.linspace(-lmbda, 0, num=n // 4)
    points.extend(list(zip(x,  x + lmbda)))
    return np.array(points)

def circle(lmbda=1, n=100):
    # 極座標系
    points = []
    for angle in np.linspace(0,np.pi/2, num=n//4):
        x = np.cos(angle) * lmbda
        y = np.sin(angle) * lmbda
        points.append((x,y))
    for angle in np.linspace(np.pi/2,np.pi, num=n//4):
        x = np.cos(angle) * lmbda
        y = np.sin(angle) * lmbda
        points.append((x,y))
    for angle in np.linspace(np.pi, np.pi*3/2, num=n//4):
        x = np.cos(angle) * lmbda
        y = np.sin(angle) * lmbda
        points.append((x,y))
    for angle in np.linspace(np.pi*3/2, 2*np.pi,num=n//4):
        x = np.cos(angle) * lmbda
        y = np.sin(angle) * lmbda
        points.append((x,y))
    return np.array(points)

def loss(b0, b1,
         a = 1,
         b = 1,
         c = 0,     # 軸の広がり
         cx = -10,  # x軸からのずれ
         cy = 5,    # y軸からのずれ
         lmbda=1.0,
         yintercept=100):
    eqn = f"{a:.2f}(b0 - {cx:.2f})^2 + {b:.2f}(b1 - {cy:.2f})^2 + {c:.2f} (b0-{cx:.2f}) (b1-{cy:.2f}) + {yintercept}"
    return lmbda * (a * (b0 - cx) ** 2 + b * (b1 - cy) ** 2) + c * (b0 - cx) * (b1 - cy) + yintercept

def loss_l1(b0,b1,a=1,b=1,c=0,cx=-10,cy=5,lmbda=1.0,yintercept=100):
    return lmbda*(a*np.abs(b0-cx) + b*np.abs(b1-cy))

#### Main Script ####
####stepsizeを変えると、表示するグラフの個数が変わります.
#### modeを'L1'にするとL1正則化、modeを'L2'にするとL2正則化になります.
mode = 'L1'
last_lmbda = 10
stepsize = 1.0
lmbdas = list(np.arange(1, last_lmbda, step=stepsize))
# lmbdas = [0]*3 + lmbdas + [last_lmbda]*3

#figの作成(この上にplotを複数描画していく)
fig = plt.figure(figsize=(10,10))
plt.subplots_adjust(wspace=0.4, hspace=2.0)
for i,lmbda in enumerate(lmbdas):
    ax = fig.add_subplot(3,3,i+1, projection='3d')
    ax.set_xlabel("$w_1$", labelpad=0)
    ax.set_ylabel("$w_2$", labelpad=0)
    ax.set_title(mode + "Regularization",fontsize=10)
    ax.tick_params(axis='x', pad=0)
    ax.tick_params(axis='y', pad=0)
    ax.set_zlim(0, 1400)

    cx = 15
    cy = -15

    ax.plot([cx], [cy], marker='x', markersize=10, color='black')
    ax.text(-20,20,800, f"$lambda={lmbda:.1f}$", fontsize=10)

    beta0 = np.linspace(-30, 30, 300)
    beta1 = np.linspace(-30, 30, 300)
    #重みの値
    B0, B1 = np.meshgrid(beta0, beta1)

    if mode=='L2':
        #正則化項
        Z1 = loss(B0, B1, a=1, b=1, c=0, cx=0, cy=0, lmbda=lmbda, yintercept=0)
        #正則化前のLoss
        Z2 = loss(B0, B1, a=5, b=5, c=0, cx=cx, cy=cy, yintercept=0)
        #正則化後のLoss
        Z = Z1 + Z2

    elif mode=='L1':
        #正則化項
        Z1 = loss_l1(B0,B1,a=5,b=5,cx=0,cy=0,lmbda=lmbda)
        #正則化前のLoss
        Z2 = loss(B0, B1, a=5, b=5, c=0, cx=cx, cy=cy, yintercept=0)
        #正則化後のLoss
        Z = Z1 + Z2

    origin = Circle(xy=(0, 0), radius=1, color='k')
    ax.add_patch(origin)
    art3d.pathpatch_2d_to_3d(origin, z=0, zdir="z")

    scale = 1.5
    vmax = 8000
    contr = ax.contour(B0, B1, Z, levels=50, linewidths=.5,
                       cmap='coolwarm',
                       zdir='z', offset=0, vmax=vmax)

    #surface plot
    j = lmbda*scale
    b0 = (j, 20-j)
    beta0 = np.linspace(-j, 25-j, 300)
    beta1 = np.linspace(-25+j, j, 300)
    B0, B1 = np.meshgrid(beta0, beta1)

    if mode=='L1':
        Z1 = loss_l1(B0,B1,a=5,b=5,cx=0,cy=0,lmbda=lmbda)
        Z2 = loss(B0, B1, a=5, b=5, c=0, cx=cx, cy=cy, yintercept=0)
        Z = Z1 + Z2

    elif mode=='L2':
        Z1 = loss(B0, B1, a=1, b=1, c=0, cx=0, cy=0, lmbda=lmbda, yintercept=0)
        Z2 = loss(B0, B1, a=5, b=5, c=0, cx=cx, cy=cy, yintercept=0)
        Z = Z1 + Z2   

    vmax = 2700
    ax.plot_surface(B0, B1, Z, alpha=1.0, cmap='coolwarm', vmax=vmax)

    #正則化項の平面可視化
    if mode=="L1":
        boundary = diamond(lmbda=lmbda)
        ax.plot(boundary[:, 0], boundary[:, 1], '-', lw=.5, c="red")

    elif mode=="L2":
        boundary = circle(lmbda=lmbda)
        ax.plot(boundary[:, 0], boundary[:, 1], '-', lw=.5, c="red")

    ax.view_init(elev=38, azim=-134)

    plt.tight_layout()

plt.subplots_adjust(hspace=0.4)
plt.show()
