import math

class Point:
    def init(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point: ({self.x}, {self.y})")

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def dist(self, other):
        delta_x = self.x - other.x
        delta_y = self.y - other.y
        return math.sqrt(delta_x2 + delta_y2)