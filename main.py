import matplotlib.pyplot as plt
import numpy as np

# importing local files
import uav_location
import random_vehicle_locations
from init import Init
from links_ground import links_ground
from links_relay import links_relay

for h in range(500, 510, 11):

    L = uav_location.uav_location(h)   # accessing the rows of the dataframe L.iloc[[i]]

    # scatter the UAV locations
    # plt.scatter(L['x'], L['y'])
    # plt.show()

    vehicle_locations = random_vehicle_locations.random_vehicle_locations()
    x_s = vehicle_locations[0]
    y_s = vehicle_locations[1]
    x_v1 = vehicle_locations[2]
    y_v1 = vehicle_locations[3]
    x_v2 = vehicle_locations[4]
    y_v2 = vehicle_locations[5]

    # plt.scatter(x_s,y_s,c="b",label="source")
    # plt.scatter(x_v1,y_v1,c="r",label="V2V 1")
    # plt.scatter(x_v2,y_v2,c="y",label="V2V 2")
    # plt.legend()
    # plt.xlim(-500, 500)
    # plt.ylim(-500, 500)
    # plt.show()

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
    sr = links_relay(L, x_s, y_s, 0, Init.p_s)
    d_sr = sr[0]
    theta_sr = sr[1]
    plos_sr = sr[2]
    pnlos_sr = sr[3]
    pathloss_sr = sr[4]
    gain_sr = sr[5]
    received_power_sr = sr[6]

    # channel information for the link V1R
    v1r = links_relay(L, x_v1, y_v1, 0, Init.p_v1)
    d_v1r = v1r[0]
    theta_v1r = v1r[1]
    plos_v1r = v1r[2]
    pnlos_v1r = v1r[3]
    pathloss_v1r = v1r[4]
    gain_v1r = v1r[5]
    received_power_v1r = v1r[6]

    # channel information for the link V2R
    v2r = links_relay(L, x_v2, y_v2, 0, Init.p_v2)
    d_v2r = v1r[0]
    theta_v2r = v2r[1]
    plos_v2r = v2r[2]
    pnlos_v2r = v2r[3]
    pathloss_v2r = v2r[4]
    gain_v2r = v2r[5]
    received_power_v2r = v2r[6]

    # channel information for the link RB
    rb = links_relay(L, Init.x_b, Init.y_b, 0, Init.p_r)
    d_rb = rb[0]
    theta_rb = rb[1]
    plos_rb = rb[2]
    pnlos_rb = rb[3]
    pathloss_rb = rb[4]
    gain_rb = rb[5]
    received_power_rb = rb[6]

    # channel information for the link RV1
    rv1 = links_relay(L, x_v1, y_v1, 0, Init.p_r)
    d_rv1 = rv1[0]
    theta_rv1 = rv1[1]
    plos_rv1 = rv1[2]
    pnlos_rv1 = rv1[3]
    pathloss_rv1 = rv1[4]
    gain_rv1 = rv1[5]
    received_power_rv1 = rv1[6]

    # channel information for the link RV1
    rv2 = links_relay(L, x_v2, y_v2, 0, Init.p_r)
    d_rv2 = rv2[0]
    theta_rv2 = rv2[1]
    plos_rv2 = rv2[2]
    pnlos_rv2 = rv2[3]
    pathloss_rv2 = rv2[4]
    gain_rv2 = rv2[5]
    received_power_rv2 = rv2[6]


