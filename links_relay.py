import numpy as np
from math import sqrt, log10
import random
from math import asin, degrees, exp, pi

# import local files
from init import Init
from db2lin import db2lin

def links_relay(L, x, y, z, p):
    # distances between relay locations and the devices on the ground
    d = np.zeros((Init.l,1))
    for i in range(Init.l):
        d[i] = sqrt(((x-(L['x'][i]))**2) + ((y-(L['y'][2]))**2) + ((z-(L['z'][2]))**2))

    # thetas between the relay locations and devices on the ground
    theta = np.zeros((Init.l,1))
    for i in range(Init.l):
        # asin returns the degree in radian
        radian = asin(L['z'][0]/d[i])
        theta[i] = degrees(radian)

    # probabilities of LoS
    plos = np.zeros((Init.l,1))
    for i in range(Init.l):
        plos[i] = 1 / (1+(Init.alpha*exp(-Init.beta*(theta[i]-Init.alpha))))

    # probabilities of NLos
    pnlos = 1 - plos

    # pathloss
    pathloss = np.zeros((Init.l,1))
    for i in range(Init.l):
        pathloss[i] = (Init.eta_los*plos[i]*((4*pi*Init.f*d[i]/Init.c))**2) + (Init.eta_nlos*pnlos[i]*((4*pi*Init.f*d[i]/Init.c))**2)

    # gain
    gain = 1 / pathloss

    # received power
    received_power = p * gain

    results = np.array([d, theta, plos, pnlos, pathloss, gain, received_power])

    return results
