class Hailstone:
    def __init__(self, sx, sy, sz, vx, vy, vz):
        self.sx = sx
        self.sy = sy
        self.sz = sz
        self.vx = vx
        self.vy = vy
        self.vz = vz

        self.alpha = vy
        self.beta = -vx
        self.charlie = vy * sx - vx * sy

    def __repr__(self):
        return "Hailstone{" + f"a={self.alpha}, b={self.beta}, c={self.charlie}" + "}"
