# 3. -------------------------------------------

year = int(input())
print(int(year % 4 == 0 != year % 100 or year % 400 == 0))

# 2. -------------------------------------------

a=int(input())
print(1 if (a%4==0 and a%100!=0) or a%400==0 else 0)

# 1. ------------------------------------------
year = int(input())
# print(year)

if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):
    print("1")
else:
    print("0")


