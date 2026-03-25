# 5. -----------------------------------
a = int(input())
b = int(input())

print(a, "+", b, "=", a + b)
print(a, "-", b, "=", a - b)
print(a, "*", b, "=", a * b)
print(a, "/", b, "=", a / b)
print(a, "//", b, "=", a // b)
print(a, "%", b, "=", a % b)
print(a, "**", b, "=", a ** b)

#4. ------------------------------------
E = int(input())
F = int(input())
G = ["+", "-", "*", "/", "//", "%", "**"]

for i in range(7):
    print(E, G[i], F, "=", eval(f"{E} {G[i]} {F}"))

#3. ------------------------------------
a=input()
b = input()
sign=["+","-","*","/","//","%","**"]
i = 0;
while(i < len(sign)):
    hap=f"{a} {sign[i]} {b}"
    result=eval(hap)
    print(f"{hap} = {result})")
    i = i + 1

#2 --------------------------
a = int(input())
b = int(input())
#print(a)
#print(b)
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")     # 나눈 몫 : 2
print(f"{a} % {b} = {a % b}")       # 나눈 나머지 : 1
print(f"{a} ** {b} = {a ** b}")     # 제곱하면 : 25

#1 --------------------------
n1 = input()
n2 = input()
print(n1)
print(n2)
print(n1, '+', n2, '=', int(n1) + int(n2))
print(n1, '-', n2, '=', int(n1) - int(n2))
print(n1, '*', n2, '=', int(n1) * int(n2))
print(n1, '/', n2, '=', int(n1) / int(n2))
print(n1, '//', n2, '=', int(n1) // int(n2))
print(n1, '%', n2, '=', int(n1) % int(n2))
print(n1, '**', n2, '=', int(n1) ** int(n2))