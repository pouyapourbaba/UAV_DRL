from intersection import isect_line_plane_v3

class IntersectionClass():
    """
        p0, p1: define the line
        p_co, p_no: define the plane:
            p_co is a point on the plane (plane coordinate).
            p_no is a normal vector defining the plane direction;
                 (does not need to be normalized).
    """
    def __init__(self, p0, p1, p_co, p_no, x, y, z):
        self.p_co = p_co
        self.p_no = p_no
        self.p1 = p0
        self.p2 = p1
        # left bottom coordinates of the plane
        self.x = x
        self.y = y
        self.z = z

    def isIntersect(self):
        isect_line_plane_v3(self.p1, self.p2, self.p_co, self.p_no)


