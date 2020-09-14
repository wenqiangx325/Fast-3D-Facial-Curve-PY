import numpy
from scipy.interpolate import griddata


def surfacePlot(x3: numpy.ndarray, y3: numpy.ndarray, z3: numpy.ndarray, res):

    x3 = x3 - x3[z3 == numpy.max(z3)]
    y3 = y3 - y3[z3 == numpy.max(z3)]
    z3 = z3 - z3[z3 == numpy.max(z3)]

    qx33, qy33 = numpy.meshgrid(
        numpy.linspace(numpy.min(x3), numpy.max(x3), res),
        numpy.linspace(numpy.min(y3), numpy.max(y3), res)
    )

    qz33 = griddata(
        numpy.array(list(zip(x3, y3))),
        z3,
        (qx33, qy33),
        method='linear'
    )
    
    return qx33, qy33, qz33
