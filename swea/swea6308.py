name, age = input(), int(input())
base_year = 2019

result_year = base_year + (100 - age)

output = "{}(은)는 {}년에 100세가 될 것입니다.".format(name, result_year)
print(output)

# 1. -----------------------------
from datetime import datetime

name = input()
age = int(input())
# now = datetime.now()
# year_minus = now.year + (100-age)
year_minus = 2079 + age
print(year_minus)
print(f"{name}(은)는 {year_minus}년에 100세가 될 것입니다.")