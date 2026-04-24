class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

lst = []
N = int(input())
for x in range(N):
    x, y = map(float, input().split())
    # print(x, y)
    p = Point(x, y)
    lst.append(p)

for x in lst:
    print(x)

lst.sort(key=lambda p: p.x)

for x in lst:
    print(x)