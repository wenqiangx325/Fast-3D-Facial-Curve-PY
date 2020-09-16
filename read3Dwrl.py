import os
import re

import numpy

def read3Dwrl(file:str):

    if not os.path.isfile(file):
        raise FileNotFoundError(f"{file}")

    points = []

    with open(file, "rb") as vrml:
        is_points = False

        for lines in vrml:
            line = lines.decode("utf-8")

            if "point [" in line:
                is_points = True
            if "]" in line and is_points is True:
                is_points = False
            
            if is_points is True:
                a = re.findall("[-+]?\d*\.\d+|\d+", line)
                if len(a) == 3:
                    points.append(list(map(float, a)))
    
    return numpy.array(points)