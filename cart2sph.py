import numpy as np
from numpy import arctan2, sqrt
import numexpr as ne

def cart2sph(x,y,z, ceval=ne.evaluate):
    """ x, y, z :  ndarray coordinates
        ceval: backend to use: 
              - eval :  pure Numpy
              - numexpr.evaluate:  Numexpr """
    azimuth = ceval('arctan2(y,x)')
    xy2 = ceval('x**2 + y**2')
    elevation = ceval('arctan2(z, sqrt(xy2))')
    r = eval('sqrt(xy2 + z**2)')
    return azimuth, elevation, r