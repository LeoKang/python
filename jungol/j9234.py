X, Y = map(float, input().split())
# print(X, Y)
match (X, Y):
    case (X, Y) if X >= 4.0 and Y >= 4.0:
        print("A grade")
    case (X, Y) if X >= 3.0 and Y >= 3.0:
        print("B grade")
    case _: 
        print("F grade")
# 1. --------------------------
x, y = map(float, input().split())
# print(x, y)

out = ""
if x>=4.0 and y>=4.0:
    out = "A grade"
elif x>=3.0 and y>=3.0:
    out = "B grade"
else:
    out = "F grade"
print(out)