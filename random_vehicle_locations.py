import random
import numpy as np

# import local files
from init import Init

def random_vehicle_locations():
    a = Init.a
    b = Init.b
    delta = Init.delta

    # x_v1, x_v2, x_s, y_v1, y_v2, y_s = 0

    # random() --> uniform distribution
    # defining the probability of locating the vehicles in either of the streets of the junction
    prob = random.random()

    if prob < 0.5:
        x_v1 = (b-a)*random.random() + a
    else:
        x_v1 = 0

    if x_v1 == 0:
        y_v1 = (b-a)*random.random() + a
        x_v2 = 0
        y_v2 = y_v1 + (delta)*random.random()+ 2 # minimum 2m distance between the vehicles
    else:
        y_v1 = 0
        y_v2 = 0
        x_v2 = x_v1 + (delta)*random.random() + 2

    if prob < 0.5:
        x_s = (b-a)*random.random() + a
    else:
        x_s = 0

    if x_s == 0:
        y_s = (b-a)*random.random() + a
    else:
        y_s = 0

    return (x_s), (y_s), x_v1, y_v1, x_v2, y_v2