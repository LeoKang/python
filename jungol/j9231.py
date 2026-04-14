score = int(input())

criteria = {90: "A", 80: "B", 70: "C", 60: "D"}

result = "F"
for point, grade in criteria.items():
    if score >= point:
        result = grade
        break

print(result)
# 2. --------------------
score=int(input())

match score // 10:
    case 10 | 9:
        print('A')
    case 8:
        print("B")
    case 7:
        print("C")
    case 6:
        print("D")
    case _:   # default와 같은 
        print('F')
# 1. -----------------
score = int(input())
print(score)

if score>=90:
    print("A")
elif score>=80:
    print("B")
elif score>=70:
    print("C")
elif score>=60:
    print("D")
else:
    print("F")