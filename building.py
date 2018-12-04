import numpy as np
import math

from intersection import isect_line_plane_v3

class Building():
    def __init__(self, x1, y1, z, w):
        self.x1 = x1 - 500
        self.y1 = y1 - 500
        self.w = w
        self.x2 = x1 + w - 500
        self.y2 = y1 + w - 500
        self.z = z

    ''' points required for
        plane1: [x, y, 0]     - [x+w, y, 0]   - [x, y, h]
        plane2: [x+w, y, 0]   - [x+w, y+w, 0] - [x+w, y, h]
        plane3: [x+w, y+w, 0] - [x, y+w, 0]   - [x+w, y+w, h]
        plane4: [x, y, 0]     - [x, y+w, 0]   - [x,  y, h]
        plane5: [x, y, h]     - [x, y+w, h]   - [x+w, y, h] '''

    # plane1: [x, y, 0] - [x+w, y, 0] - [x, y, z]
    def plane1(self):
        p1 = np.array([self.x1, self.y1, 0])
        p2 = np.array([self.x1+self.w, self.y1, 0])
        p3 = np.array([self.x1, self.y1, self.z])
        n = np.cross(p2 - p1, p3 - p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n,n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i]/abs_n
        # return one point on the plane and the perpendicular normal vector of the plane
        return p1, n

    # plane2: [x+w, y, 0] - [x+w, y+w, 0] - [x+w, y, z]
    def plane2(self):
        p1 = np.array([self.x1+self.w, self.y1, 0])
        p2 = np.array([self.x1+self.w, self.y1+self.w, 0])
        p3 = np.array([self.x1+self.w, self.y1, self.z])
        n = np.cross(p2 - p1, p3 - p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n,n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i]/abs_n
        # return one point on the plane and the perpendicular normal vector of the plane
        return p1, n

    # plane3: [x+w, y+w, 0] - [x, y+w, 0] - [x+w, y+w, z]
    def plane3(self):
        p1 = np.array([self.x1+self.w, self.y1+self.w, 0])
        p2 = np.array([self.x1, self.y1+self.w, 0])
        p3 = np.array([self.x1+self.w, self.y1+self.w, self.z])
        n = np.cross(p2 - p1, p3 - p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n,n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i]/abs_n
        # return one point on the plane and the perpendicular normal vector of the plane
        return p1, n

    # plane4: [x, y, 0] - [x, y+w, 0] - [x,  y, z]
    def plane4(self):
        p1 = np.array([self.x1, self.y1, 0])
        p2 = np.array([self.x1, self.y1+self.w, 0])
        p3 = np.array([self.x1, self.y1, self.z])
        n = np.cross(p2 - p1, p3 - p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n,n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i]/abs_n
        # return one point on the plane and the perpendicular normal vector of the plane
        return p1, n

    # plane5: [x, y, z] - [x, y+w, z] - [x+w, y, z]
    def plane5(self):
        p1 = np.array([self.x1, self.y1, self.z])
        p2 = np.array([self.x1, self.y1+self.w, self.z])
        p3 = np.array([self.x1+self.w, self.y1, self.z])
        n = np.cross(p2 - p1, p3 - p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n,n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i]/abs_n
        # return one point on the plane and the perpendicular normal vector of the plane
        return p1, n