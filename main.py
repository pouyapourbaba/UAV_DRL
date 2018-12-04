import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# importing local files
import uav_location
import random_vehicle_locations
from init import Init
from links_ground import links_ground
from links_relay import links_relay

for h in range(500, 510, 11):

    L = uav_location.uav_location(h)   # accessing the rows of the dataframe L.iloc[[i]]

    # scatter the UAV locations
    plt.scatter(L['x'], L['y'])
    plt.show()

    x_s, y_s, x_v1, y_v1, x_v2, y_v2 = random_vehicle_locations.random_vehicle_locations()
    print("xs: {}, ys: {}".format(x_s, y_s))
    print("x1: {}, y1: {}".format(x_v1, y_v1))
    print("x2: {}, y2: {}".format(x_v2, y_v2))

    plt.scatter(x_s,y_s,c="b",label="source")
    plt.scatter(x_v1,y_v1,c="r",label="V2V 1")
    plt.scatter(x_v2,y_v2,c="y",label="V2V 2")
    plt.legend()
    plt.xlim(-550, 550)
    plt.ylim(-550, 550)
    plt.show()

    # channel gain, distance, and pathloss between source and V2V vehicles
    sv1 = links_ground(x_s,y_s,x_v1,y_v1)
    gain_sv1 = sv1[0]
    d_sv1 = sv1[1]
    pathloss_sv1 = sv1[2]

    sv2 = links_ground(x_s,y_s,x_v2,y_v2)
    gain_sv2 = sv2[0]
    d_sv2 = sv2[1]
    pathloss_sv2 = sv2[2]

    # channel gain, distance, and pathloss between V2V vehicles
    v2v= links_ground(x_v1, y_v1, x_v2, y_v2)
    gain_v2v = v2v[0]
    d_v2v = v2v[1]
    pathloss_v2v = v2v[2]

    # channel information for the link SR
    d_sr, theta_sr, plos_sr, pnlos_sr, pathloss_sr, gain_sr, received_power_sr = links_relay(L, x_s, y_s, 0, Init.p_s)

    # channel information for the link V1R
    d_v1r, theta_v1r, plos_v1r, pnlos_v1r, pathloss_v1r, gain_v1r, received_power_v1r = links_relay(L, x_v1, y_v1, 0, Init.p_v1)

    # channel information for the link V2R
    d_v2r, theta_v2r, plos_v2r, pnlos_v2r, pathloss_v2r, gain_v2r, received_power_v2r = links_relay(L, x_v2, y_v2, 0, Init.p_v2)

    # channel information for the link RB
    d_rb, theta_rb, plos_rb, pnlos_rb, pathloss_rb, gain_rb, received_power_rb = links_relay(L, Init.x_b, Init.y_b, 0, Init.p_r)

    # channel information for the link RV1
    d_rv1, theta_rv1, plos_rv1, pnlos_rv1,  pathloss_rv1,  gain_rv1, received_power_rv1= links_relay(L, x_v1, y_v1, 0, Init.p_r)

    # channel information for the link RV1
    d_rv2, theta_rv2, plos_rv2, pnlos_rv2, pathloss_rv2, gain_rv2, received_power_rv2 = links_relay(L, x_v2, y_v2, 0, Init.p_r)

    ''' building the discrete sections of the street '''