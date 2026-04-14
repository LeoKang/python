hour = int(input())
# print(hour)
is_pm = bool(hour // 12)
print("PM" if is_pm else "AM")
# 1. --------------------
time = int(input())
# print(time)

res = ""
if time < 12:
    res = "AM"
else:
    res = "PM"
print(res)