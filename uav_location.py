import numpy as np
import pandas as pd

# import local files

# defining the locations of the UAV
def uav_location(h):
    l = 400    # number of locations
    k = 0
    x = np.zeros([l])   # placeholder for x coordinates
    y = np.zeros([l])   # placeholder for y coordinates
    z = np.zeros([l])   # placeholder for z coordinates

    # looping through the limits and filling the placeholders of the coordinates
    # for i in range(1, 116, 6):
    #     for j in range(1, 116, 6):
    #         x[k] = np.array([i-58])
    #         y[k] = np.array([j-58])
    #         z[k] = h
    #         k += 1

    for i in range(4, 464, 24):
        for j in range(4, 464, 24):
            x[k] = np.array([i - 232])
            y[k] = np.array([j - 232])
            z[k] = h
            k += 1

    # converting the numpy arrays x, y, and z into pandas dataframe
    L = pd.DataFrame({"x": x, "y": y, "z": z})
    return L