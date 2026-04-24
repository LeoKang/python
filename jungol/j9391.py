h, m = map(int, input().split())
# print(h, m)
is_pm = h // 12
signal = ["AM", "PM"][is_pm]

h = h - 12 if h >= 13 else h

print("%02d : %02d %s" % (h, m, signal))

# 1. ---------------------------------

h, m = map(int, input().split())
ampm = "M"
if h>=12:
    ampm = "PM"
else:
    ampm = "AM"

if h>=13:
    h-=12

print(f"{h:02d} : {m:02d} {ampm}")