print("PASS" if int(input())>=60 else "FAIL")
# 3. --------------------------
class P:
    def __init__(self,A):
        self.A = A
    def OK(self):
        if 60<=self.A:
            print("PASS")
        else:
            print("FAIL")

a = int(input())
p=P(a)
p.OK()

# 2. -----------------------
score = int(input())
# print(score)
results = ["FAIL", "PASS"]
print(results[score >= 60])

# 1. --------------------
# score = int(input())
# if score>= 60:
#     print("PASS")
# else:
#     print("FAIL")