import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from sph2cart import sph2cart
from cart2sph import cart2sph
from surfacePlot import surfacePlot

def visualizeCurve(vertex, res, curveSet):

    qx, qy, qz = surfacePlot(vertex, res)
    th, phi, r = cart2sph(qx.flatten('F'), qy.flatten('F'), qz.flatten('F'))
    xxl, yyl, zzl = sph2cart(th, phi, r)

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.plot(xxl,yyl,zzl, "ro", markersize=5, mfc='none')

    for curve in curveSet:
        x, y, z = zip(*curve)
        ax.plot(x, y, z, 'ks', markersize="5", mfc='none')
    plt.show()
