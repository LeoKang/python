print("Middle School" if int(input()) >= 13 else "Elementary School")

# 2. -------------------------
age = int(input())
# print(age)
schools = ["Elementary School", "Middle School"]
print(schools[age >= 13])

# 1. -------------------------
age = int(input())
# print(age)

if age >= 13:
    print("Middle School")
else:
    print("Elementary School")