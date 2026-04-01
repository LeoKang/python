def get_results(a, b):
    return {
        "합": a + b,
        "차": abs(a - b)
    }

n1, n2 = map(int, input().split())
res = get_results(n1, n2)

print(f"두 수의 합 = {res['합']}")
print(f"두 수의 차 = {res['차']}")

# 5. ------------------------------------
N, M = map(int,input().split())
Y = abs(N-M)
def f():
    print(f'두 수의 합 = {N+M}')
    print(f'두 수의 차 =',Y)
f()
# 4. ---------------------------------

# def A(x, y):
#     return x + y

# def B(x, y):
#     return abs(x - y)

# n1, n2 = map(int, input().split())

# print(f"두 수의 합 = {A(n1, n2)}")
# print(f"두 수의 차 = {B(n1, n2)}")

# # 3. --------------------------------

# class Chi:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b

#     def Q (self):
#         return self.a+self.b

#     def W (self):
#         return abs(self.a-self.b)

#     def E (self):
#         print(f"두 수의 합 = {self.Q()}")
#         print(f"두 수의 차 = {self.W()}")

# hap,cha=map(int, input().split())

# ZIP=[hap,cha]

# p=Chi(hap,cha)

# p.E()

# # 2. -------------------------------
# def calc(p1, p2):
#     sum = p1 + p2
#     minus = 0
#     if p1 > p2:
#         minus = p1 - p2
#     else:
#         minus = p2 - p1

#     return [sum, minus]

# r1, r2 = calc(50, 30)
# print(r1, r2)

# # 1. ----------------------------------
# # n1, n2 = map(int, input().split())
# # # print(n1, n2)

# # def func_plus(p1, p2):
# #     return p1 + p2

# # ret1 = func_plus(n1, n2)
# # print(f"두 수의 합 = {ret1}")

# # def func_minus(p1, p2):
# #     if p1>p2:
# #         return p1-p2
# #     else:
# #         return p2-p1

# # ret2 = func_minus(n1, n2)
# # print(f"두 수의 차 = {ret2}")
