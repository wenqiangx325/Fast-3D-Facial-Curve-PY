import numpy


def sph2cart(alpha, beta, r):
    x = r * numpy.cos(beta) * numpy.cos(alpha)
    y = r * numpy.cos(beta) * numpy.sin(alpha)
    z = r * numpy.sin(beta)
    return x, y, z
