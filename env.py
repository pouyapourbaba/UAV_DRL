from building import Building
import numpy as np
import math

# my own scripts
from intersection import isect_line_plane_v3
import uav_location

# 3d environment figure libs
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib

L = uav_location.uav_location(200)

# range of the area that buildings are located starting from the
# origin, each building is 50m long and 50m wide
x = range(0,1000,50)
y = range(0,1000,50)
w = 50 # width of each building

# number of buildings
nOfB = 400

# random height of the buildings
h = np.zeros(nOfB)
for l in range(nOfB):
    h[l] = abs(np.random.rayleigh(20))


# Building objects
buildings = []
k = 0 # index of the building
for i in range(int(math.sqrt(nOfB))):
    for j in range(int(math.sqrt(nOfB))):
        if i==9 or i==10:
            buildings.append(Building(0, 0, 0, w))
        elif j==9 or j==10:
            buildings.append(Building(0, 0, 0, w))
        else:
            buildings.append(Building(x[i], y[j], h[k], w))
        k = k + 1

# arbitrary vehicle location
# v = [-475, -520, 25]
v = [0,0,0]

# intersection of the UAV links and the buildings
# losOrNlos = np.ones(400) # LOS = 1, NLOS = 0
# for u in range(len(L)):
#     i = 0
#     for b in buildings:
#         plane1, n1 = b.plane1()
#         plane2, n2 = b.plane2()
#         plane3, n3 = b.plane3()
#         plane4, n4 = b.plane4()
#         plane5, n5 = b.plane5()
#         u_loc = np.array([L.loc[i]['x'],L.loc[i]['y'],L.loc[i]['z']])
#         u_loc = [0, 2, 22]
#
#         intersection1 = isect_line_plane_v3(v, u_loc, plane1, n1)
#         intersection2 = isect_line_plane_v3(v, u_loc, plane2, n2)
#         intersection3 = isect_line_plane_v3(v, u_loc, plane3, n3)
#         intersection4 = isect_line_plane_v3(v, u_loc, plane4, n4)
#         intersection5 = isect_line_plane_v3(v, u_loc, plane5, n5)
#         # check the intersection with the first plane
#         if intersection1 is not None:
#             if intersection1[0] >= b.x1 and intersection1[0] <= b.x1 and intersection1[1] == b.y1 and intersection1[2] >= 0 and intersection1[2] <= b.z:
#                 losOrNlos[i] = 0
#             # else:
#             #     losOrNlos[i] = 1
#         # check the intersection with the second plane
#         elif intersection2 is not None:
#             if intersection2[0] == b.x2 and intersection2[1] >= b.y1 and intersection2[1] <= b.y2 and intersection1[2] >= 0 and intersection1[2] <= b.z:
#                 losOrNlos[i] = 0
#             # else:
#             #     losOrNlos[i] = 1
#         # check the intersection with the third plane
#         elif intersection3 is not None:
#             if intersection3[0] >= b.x1 and intersection3[0] <= b.x1 and intersection3[1] == b.y2 and intersection3[2] >= 0 and intersection3[2] <= b.z:
#                 losOrNlos[i] = 0
#             # else:
#             #     losOrNlos[i] = 1
#         # check the intersection with the fourth plane
#         elif intersection4 is not None:
#             if intersection4[0] == b.x1 and intersection4[1] >= b.y1 and intersection4[1] <= b.y2 and intersection4[2] >= 0 and intersection4[2] <= b.z:
#                 losOrNlos[i] = 0
#             # else:
#             #     losOrNlos[i] = 1
#         # check the intersection with the fifth plane
#         elif intersection5 is not None:
#             if intersection5[0] >= b.x1 and intersection5[0] <= b.x2 and intersection5[1] >= b.y1 and intersection5[1] <= b.y2 and intersection5[2] == b.z:
#                 losOrNlos[i] = 0
#             # else:
#             #     losOrNlos[i] = 1
#         else:
#             losOrNlos[i] = 1
#         i = i + 1
#
# print(losOrNlos)

# print("(x1, y1):", "(", buildings[0].x1, ",", buildings[0].y1, ")")
# print("(x2, y2):", "(", buildings[0].x2, ",", buildings[0].y1, ")")
# print("h:", buildings[0].z)
#
# print("(x1, y1):", "(", buildings[1].x1, ",", buildings[1].y1, ")")
# print("(x2, y2):", "(", buildings[1].x2, ",", buildings[1].y1, ")")
# print("h:", buildings[1].z)

# check the intersection
p1, n1 = buildings[0].plane1()
#print(p1)
#print(n1)


# p2, n2 = buildings[0].plane2(buildings[0].x1, buildings[0].y1, buildings[0].h, buildings[0].w)
# print(n2)

# print(buildings[1].x1, buildings[1].x2)
# print(buildings[1].y1, buildings[1].y2)


#Right now, I have prepared the functions inside the Building class to calculate the normal functions of 5 main surfaces of the buildings (not the bottom surface).

# I will use the normal vectors and the point on the plane (p1 and n from the plane1,...,plane5 function in the Building class) in the isect_line_plane_v3 function
# to find out if the link from the UAV intercepts with any of the surfaces of the buildings. If no intercept is recognized the link is LoS, otherwise, the link is
# a NLoS link.



# find out if the vector returned by the function "isect_line_plane_v3" is the point of intersection
ins = isect_line_plane_v3([-225,-300,25], [-225,-200,25], p1, n1)
#ins = isect_line_plane_v3([0,0,0], [10, 0, 25], p1, n1)
if ins is None:
    print("Not Intersected")
else:
    if (ins[0]>=buildings[100].x1 and ins[0]<=buildings[100].x2):
        if (ins[1]>=buildings[100].y1 and ins[1]<=buildings[100].y2):
            print('intersected')
            print(ins)

# fig = plt.figure()
# ax1 = fig.add_subplot(111, projection='3d')
#
# xpos = np.zeros(nOfB)
# ypos = np.zeros(nOfB)
# for i in range(nOfB):
#     xpos[i] = buildings[i].x1
#     ypos[i] = buildings[i].y1
#
# zpos = np.zeros(nOfB)
#
# dx = np.ones(nOfB) * 50
# dy = np.ones(nOfB) * 50
# dz = h
#
# ax1.bar3d(xpos,ypos,zpos, dx,dy,dz)
# # if (ins[0]>=buildings[100].x1 and ins[0]<=buildings[100].x2) and (ins[1]>=buildings[100].y1 and ins[1]<=buildings[100].y2):
# #     ax1.scatter(ins[0],ins[1],ins[2])
# ax1.scatter(L['x'], L['y'], L['z'], c='r')
# ax1.scatter(v[0], v[1], v[2], c="green")
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()