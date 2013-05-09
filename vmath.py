from math import *

class v2():
    @staticmethod
    def from_tuple(t):
        return v2(t[0], t[1])

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def scale(self, s):
        self.x *= s
        self.y *= s

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def length(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def length_squared(self):
        return (self.x * self.x + self.y * self.y)

    def absolute(self):
        return v2(abs(self.x), abs(self.y))

    def normalize(self):
        try:
            self /= self.length()
        except ZeroDivisionError:
            pass
        return self

    def to_tuple(self):
        return (self.x, self.y)

    def clone(self):
        return v2(self.x, self.y)

    def __iter__(self):
        return iter((self.x, self.y))

    def __repr__(self):
        return 'v2(%s, %s)' % (self.x, self.y)

    def __add__(self, other):
        return v2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return v2(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __mul__(self, other):
        return v2(self.x * other, self.y * other)

    def __imul__(self, other):
        self.x *= other
        self.y *= other
        return self

    def __div__(self, other):
        return v2(self.x / other, self.y / other)

    def __idiv__(self, other):
        self.x /= other
        self.y /= other
        return self

    def __neg__(self):
        return v2(-self.x, -self.y)

