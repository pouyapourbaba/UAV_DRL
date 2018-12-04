from building import Building
import numpy as np
import math

# my own scripts
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



''' PLOTS AND INFORMATION '''
print("(x1, y1):", "(", buildings[0].x1, ",", buildings[0].y1, ")")
print("(x2, y2):", "(", buildings[0].x2, ",", buildings[0].y1, ")")
print("h:", buildings[0].h)

print("(x1, y1):", "(", buildings[1].x1, ",", buildings[1].y1, ")")
print("(x2, y2):", "(", buildings[1].x2, ",", buildings[1].y1, ")")
print("h:", buildings[1].h)

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

xpos = np.zeros(nOfB)
ypos = np.zeros(nOfB)
for i in range(nOfB):
    xpos[i] = buildings[i].x1
    ypos[i] = buildings[i].y1

zpos = np.zeros(nOfB)

dx = np.ones(nOfB) * 50
dy = np.ones(nOfB) * 50
dz = h

ax1.bar3d(xpos,ypos,zpos, dx,dy,dz)
ax1.scatter(L['x'], L['y'], L['z'], c='r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()