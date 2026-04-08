class Honeycomb:
    def __init__(self):
        self.layer = 1
        self.max_room = 1

    def expand(self):
        self.max_room += 6 * self.layer
        self.layer += 1

    def find_dist(self, target):
        while target > self.max_room:
            self.expand()
        return self.layer

h = Honeycomb()
print(h.find_dist(int(input())))
# 1. -------------------------------
N = int(input())
# print(N)
boundary = 1
x = 1

while True:
    if N <= boundary:
        break;
    boundary = boundary + (6 * x)
    x = x + 1
    # print(x, boundary)

print(x)
