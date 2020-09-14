
from surfacePlot import surfacePlot


def exFacialCurve(vertex:tuple, res:int=100, p:float=2, rp:list=list(range(30,80,10)), npt):

    [qx, qy, qz] = surfacePlot(vertex[0], vertex[1], vertex[2], res)
    pass
