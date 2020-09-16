from read3Dwrl import read3Dwrl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import re


file = "./faceFolder/refFace.wrl"

points = read3Dwrl(file)


print(points)
#3D Plotting
x,y,z = zip(*points)
fig = plt.figure()
ax = Axes3D(fig)
ax.plot(x,y,z, "bo", markersize=1)
plt.show()