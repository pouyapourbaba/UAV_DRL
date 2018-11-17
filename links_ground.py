import numpy as np
from math import sqrt, log10, pow
import random

# import local files
from init import Init
from db2lin import db2lin

def links_ground(x1,y1,x2,y2):
    PL_0 = Init.PL_0
    d_b = Init.d_b
    n1 = Init.n1
    d_0 = Init.d_0
    n2 = Init.n2

    # distance between the vehicles
    d = sqrt(pow((x1-x2),2) + pow((y1-y2),2))

    # pathloss between vehicles
    if d <= d_b:
        pathloss = PL_0 + 10 * n1 * log10(d / d_0) + random.normalvariate(0, 4.15) # zero mean with standard deviation sqrt(4.15)
        pathloss = db2lin(pathloss)
    else:
        pathloss = PL_0 + 10 * n1 * log10(d_b / d_0) + 10 * n2 * log10(d / d_b) + random.normalvariate(0, 4.15)
        pathloss = db2lin(pathloss)

    # gain of the link between vehicles
    gain = 1 / pathloss

    results = np.array([gain, d, pathloss])
    return results