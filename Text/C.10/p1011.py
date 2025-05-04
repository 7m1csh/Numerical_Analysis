import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import warnings
lmbda = 2
w,h = 10,10
#パラメータ(ここでは二変数のみ)
beta0 = np.linspace(-w, w, 100)
beta1 = np.linspace(-h, h, 100)
B0, B1 = np.meshgrid(beta0, beta1)
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
         c = 0,     # a～c 軸の広がり
         cx = -10,  # x軸の中心からのずれ
         cy = 5):   # y軸の中心からのずれ
    return a * (b0 - cx) ** 2 + b * (b1 - cy) ** 2 + c * (b0 - cx) * (b1 - cy)
def select_parameters(lmbda, reg, force_symmetric_loss, force_one_nonpredictive):
    while True:
        a = np.random.random() * 10
        b = np.random.random() * 10
        c = np.random.random() * 4 - 1.5
        if force_symmetric_loss:
            b = a # 対称化
            c = 0
        elif force_one_nonpredictive:
            if np.random.random() > 0.5:
                a = np.random.random() * 15 - 5
                b = .1
            else:
                b = np.random.random() * 15 - 5
                a = .1
            c = 0
        x, y = 0, 0
        #L1正則化の時
        if reg=='L1':
            while np.abs(x) + np.abs(y) <= lmbda:
                x = np.random.random() * 2 * w - w
                y = np.random.random() * 2 * h - h
        #L2正則化の時
        else:
            while np.sqrt(x**2 + y**2) <= lmbda:
                x = np.random.random() * 2 * w - w
                y = np.random.random() * 2 * h - h
        #Lossの値(Z軸の値)
        Z = loss(B0, B1, a=a, b=b, c=c, cx=x, cy=y)
        loss_at_min = loss(x, y, a=a, b=b, c=c, cx=x, cy=y)
        if (Z >= loss_at_min).all(): #鞍点がない場合
            break
    return Z, a, b, c, x, y
def plot_loss(boundary, reg,
              boundary_color='#2D435D',
              boundary_dot_color='#E32CA6',
              force_symmetric_loss=False, force_one_nonpredictive=False,
              show_contours=True, contour_levels=50, show_loss_eqn=False,
              show_min_loss=True,idx=None,fig=None,ax=None,num_trials=None):
    Z, a, b, c, x, y = select_parameters(lmbda, reg,
                          force_symmetric_loss=force_symmetric_loss,
                          force_one_nonpredictive=force_one_nonpredictive)
    eqn = f"{a:.2f}(b0 - {x:.2f})^2 + {b:.2f}(b1 - {y:.2f})^2 + {c:.2f} b0 b1"
    n_col = 5
    if show_loss_eqn:
        ax[idx//n_col, idx%n_col].set_title(eqn, fontsize=10)
    ax[idx//n_col, idx%n_col].set_xlabel("x", fontsize=8, labelpad=0)
    ax[idx//n_col, idx%n_col].set_ylabel("y", fontsize=8, labelpad=-10)
    ax[idx//n_col, idx%n_col].set_xticks([-10,-5,0,5,10])
    ax[idx//n_col, idx%n_col].set_yticks([-10,-5,0,5,10])
    ax[idx//n_col, idx%n_col].set_xlabel(r"$w_1$", fontsize=8)
    ax[idx//n_col, idx%n_col].set_ylabel(r"$w_2$", fontsize=8)
    shape = ""
    if force_symmetric_loss:
        shape = "symmetric "
    elif force_one_nonpredictive:
        shape = "orthogonal "
    ax[idx//n_col, idx%n_col].set_title(f"{reg} constraint w/{shape}loss function", fontsize=8)
    if show_contours:
        ax[idx//n_col, idx%n_col].contour(B0, B1, Z, levels=contour_levels, linewidths=1.0, cmap='coolwarm')
    else:
        ax[idx//n_col, idx%n_col].contourf(B0, B1, Z, levels=contour_levels, cmap='coolwarm')
    # 軸の描画
    ax[idx//n_col, idx%n_col].plot([-w,+w],[0,0], '-', c='k', lw=.5)
    ax[idx//n_col, idx%n_col].plot([0, 0],[-h,h], '-', c='k', lw=.5)
    # 境界の描画
    if boundary is not None:
        ax[idx//n_col, idx%n_col].plot(boundary[:,0], boundary[:,1], '-', lw=1.5, c=boundary_color)
    # Lossの中心点の作図
    if show_min_loss:
        ax[idx//n_col, idx%n_col].scatter([x],[y], s=90, c='k')
    # 境界点の図示
    eqn = f"{a:.2f}(b0 - {x:.2f})^2 + {b:.2f}(b1 - {y:.2f})^2 + {c:.2f} (b0-{x:.2f}) (b1-{y:.2f})"
    if boundary is not None:
        losses = [loss(*edgeloc, a=a, b=b, c=c, cx=x, cy=y) for edgeloc in boundary]
        minloss_idx = np.argmin(losses)
        coeff = boundary[minloss_idx]
        ax[idx//n_col, idx%n_col].scatter([coeff[0]], [coeff[1]], s=90, c=boundary_dot_color)
        if force_symmetric_loss:
            if reg=='L2':
                ax[idx//n_col, idx%n_col].plot([x,0],[y,0], ':', c='k')
            else:
                ax[idx//n_col, idx%n_col].plot([x,coeff[0]],[y,coeff[1]], ':', c='k')
def show_example(reg, force_symmetric_loss=False, force_one_nonpredictive=False,num_trials=None):
    if num_trials <=5:
        fig,ax = plt.subplots(1,5,figsize=(10,2),squeeze=False)
    elif num_trials > 5 and num_trials<=10:
        fig,ax = plt.subplots(2,5,figsize=(10,4))
    elif num_trials > 10 and num_trials<=15:
        fig,ax = plt.subplots(3,5,figsize=(10,6))
        fig.subplots_adjust(hspace=0.6, wspace=0.4)
    if reg == 'L1':
        boundary = diamond(lmbda=lmbda, n=100)
    else:
        boundary = circle(lmbda=lmbda, n=100)
    for i in range(num_trials):
        plot_loss(boundary=boundary, reg=reg,
                  force_symmetric_loss=force_symmetric_loss,
                  force_one_nonpredictive=force_one_nonpredictive,
                  contour_levels=contour_levels,idx=i,fig=fig,ax=ax,num_trials=num_trials)
        shape_fname = ""
        if force_symmetric_loss:
            shape_fname = "symmetric-"
        elif force_one_nonpredictive:
            shape_fname = "orthogonal-"
        plt.tight_layout()
    #余分なaxesを消去
    if num_trials%5!=0:
        #余白数の計算
        k = 5*(1 + num_trials//5)-num_trials
        for i in range(k):
            fig.delaxes(ax[num_trials//5][-i-1])
    plt.show()
def just_contour():
    contour_levels = 400
    cx, cy = 4, .8
    beta0 = np.linspace(-w, w, 300)
    beta1 = np.linspace(-h, h, 300)
    B0, B1 = np.meshgrid(beta0, beta1)
    Z = loss(B0, B1, a=9, b=1, c=4.5, cx=cx, cy=cy)
    fig, ax = plt.subplots(1, 1, figsize=(8, 8))
    ax.set_xlim(-2,8)
    ax.set_ylim(-2,8)
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.set_xlabel(r"$eta_1$", fontsize=12)
    # ax.set_ylabel(r"$eta_2$", fontsize=12)
    ax.contour(B0, B1, Z, levels=contour_levels, linewidths=.8, cmap='coolwarm', vmax=380)
    # Draw axes
    ax.plot([-w, +w], [0, 0], '-', c='k', lw=.5)
    ax.plot([0, 0], [-h, h], '-', c='k', lw=.5)
    lmbda = 2.58
    boundary_color = '#2D435D'
    boundary = diamond(lmbda=lmbda, n=200)
    ax.plot(boundary[:, 0], boundary[:, 1], '-', lw=.5, c=boundary_color)
    boundary = circle(lmbda=lmbda, n=200)
    ax.plot(boundary[:, 0], boundary[:, 1], '-', lw=.5, c=boundary_color)
    # Draw center of loss func
    ax.scatter([cx], [cy], s=20, c='k')
    plt.tight_layout()
    plt.show()
## main script ##
####以下の値で表示内容を切り替えてください.####
#n_trialsは15以下の数字を入力してください
n_trials = 12
contour_levels=50
mode = "L1"
s = 0
##############################################
np.random.seed(s)
show_example(reg=mode,num_trials=n_trials)
