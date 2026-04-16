weight = float(input())
# print(weight)

classes = [
    (50.80, "Flyweight"),
    (61.23, "Lightweight"),
    (72.57, "Middleweight"),
    (88.45, "Cruiserweight")
]

res = "Heavyweight"
for limit, name in classes:
    if weight <= limit:
        res = name
        break
print(res)
# 1. ----------------------------
weight = float(input())
# print(weight)

if weight<=50.8:
    print("Flyweight")
elif weight<=61.23:
    print("Lightweight")
elif weight<=72.57:
    print("Middleweight")
elif weight<=88.45:
    print("Cruiserweight")
else:
    print("Heavyweight")
