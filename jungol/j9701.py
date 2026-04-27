class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __truediv__(self, other):
        return Point(self.x / other.x, self.y / other.y)

    def __str__(self):
         return f"({self.x:.1f}, {self.y:.1f})"


x, y = map(float, input().split())
# print(x, y)
p1 = Point(x, y)
x, y = map(float, input().split())
# print(x, y)
p2 = Point(x, y)

add = p1 + p2
print(f"add =", add)
sub = p1 - p2
print(f"sub =", sub)
center = add / Point(2.0, 2.0)
print(f"center =", center)