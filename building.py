import numpy as np
import math

from intersection import isect_line_plane_v3

class Building():
    def __init__(self, x1, y1, h, w):
        self.x1 = x1 - 500
        self.y1 = y1 - 500
        self.w = w
        self.x2 = x1 + w - 500
        self.y2 = y1 + w - 500
        self.h = h

    def plane1(self, x1, y1, h, w):
        x = x1
        y = y1
        p1 = np.array([x,   y,   0])
        p2 = np.array([x+w, y,   0])
        p3 = np.array([x,   y,   h])
        n = np.cross(p2 - p1, p3 - p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n,n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i]/abs_n

        return p1, n

    def plane2(self, x1, y1, h, w):
        x = x1
        y = y1
        p1 = np.array([x+w, y,   0])
        p2 = np.array([x+w, y+w, 0])
        p3 = np.array([x+w, y,   h])
        n = np.cross(p2 - p1, p3 - p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n, n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i] / abs_n

        return p1, n

    def plane3(self, x1, y1, h, w):
        x = x1
        y = y1
        p1 = np.array([x+w, y+w, 0])
        p2 = np.array([x,   y+w, 0])
        p3 = np.array([x+w, y+w, h])
        n = np.cross(p2 - p1, p3 - p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n, n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i] / abs_n

        return p1, n

    def plane4(self, x1, y1, h, w):
        x = x1
        y = y1
        p1 = np.array([x,  y,   0])
        p2 = np.array([x,  y+w, 0])
        p3 = np.array([x,  y,   h])
        n = np.cross(p2-p1, p3-p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n, n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i] / abs_n

        return p1, n

    def plane5(self, x1, y1, h, w):
        x = x1
        y = y1
        p1 = np.array([x,   y,   h])
        p2 = np.array([x,   y+w, h])
        p3 = np.array([x+w, y,   h])
        n = np.cross(p2 - p1, p3 - p1)
        # normalizing the vector n
        abs_n = math.sqrt(np.inner(n, n))
        for i in range(3):
            if n[i] != 0:
                n[i] = n[i] / abs_n

        return p1, n