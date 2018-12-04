import numpy as np
import math

class Building():
    def __init__(self, x1, y1, h, w):
        self.x1 = x1 - 500
        self.y1 = y1 - 500
        self.w = w
        self.x2 = x1 + w - 500
        self.y2 = y1 + w - 500
        self.h = h