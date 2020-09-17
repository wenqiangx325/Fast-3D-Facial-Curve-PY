import os
import glob
from matplotlib import markers

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from read3Dwrl import read3Dwrl
from exFacialCurve import exFacialCurve
from visualizeCurve import visualizeCurve

faceFoldr = 'faceFolder'
fileType = ".wrl"
folderContent = glob.glob(os.path.join(faceFoldr, f"*{fileType}"))

for i, file in enumerate(folderContent):

    try:
        vertex = read3Dwrl(file)
    except Exception:
        continue
    
    res = 100

    sel = 1

    lvSet = np.arange(0, 360, 20)

    npt = 20

    curVSet = exFacialCurve(vertex, res, sel, lvSet, npt)

    visualizeCurve(vertex, res, curVSet)
    


