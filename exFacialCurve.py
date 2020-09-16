
import enum
import numpy
from numpy.core import numeric

from sph2cart import sph2cart
from cart2sph import cart2sph
from surfacePlot import surfacePlot


def exFacialCurve(vertex: numpy.array, res: int, p: float, rp: numpy.array, npt: int):

    nth = rp
    qx, qy, qz = surfacePlot(vertex, res)
    th, phi, r = cart2sph(qx.flatten('F'), qy.flatten('F'), qz.flatten('F'))

    th = th[~ numpy.isnan(r)]
    phi = phi[~numpy.isnan(r)]
    r = r[~numpy.isnan(r)]

    if p == 1:
        for i, t in enum(nth):
            piu = nth[t]
            if piu > 180:
                theta = (180-piu)/57.7
            else:
                theta = piu/57.7
            
            xc = th[th>theta and th<theta+0.05]
            yc = phi[th>theta and th<theta+0.05]
            zc = r[th>theta and th<theta+0.05]

            xx, yy, zz = sph2cart(xc, yc, zc)

    else:
        cdata2 = list()
        for i, t in enumerate(nth):
            lev = nth[i]
            # print(r > lev and r < lev+2)
            xc = th[numpy.array(r > lev) & numpy.array(r < lev+2)]
            yc = phi[numpy.array(r > lev) & numpy.array(r < lev+2)]
            zc = r[numpy.array(r > lev) & numpy.array(r < lev+2)]

            xx, yy, zz = sph2cart(xc, yc, zc)

            cdata2.append(numpy.array([xx, yy, zz]).T)
        return cdata2
