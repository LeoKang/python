num1, num2 = map(int, input().split())
# print(num1, num2)

quotient = num1 // num2     # 나눈 몫
remainder = num1 % num2     # 나머지

print(f"{num1} / {num2} = {quotient} ... {remainder}")

# a, b = map(int, input().split())
# print(f"{a} / {b} = {a//b} ... {a%b}")

# print(a/b)  # result
# print(a//b) # 몫
# print(a%b)  # 나머지

# a, b = input().split()
# na = int(a)
# nb = int(b)
# print(a, '/', b, '=', na//nb, '...', na%nb) 