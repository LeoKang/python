num = str(input())
sum = 0
for i in range(4):
    sum += int(num)
    num+=num[i]
print(sum)
# 4. ---------------------
a = input()
print(int(a) + int(a * 2) + int(a * 3) + int(a * 4))
# 3. -------------------
a = int(input())
print((a*4)+(a*10)*3+(a*100)*2+(a*1000))

# 2. --------------------
a_Str = input()
# print(a_Str)

term1 = int(a_Str)
term2 = int(a_Str * 2)
term3 = int(a_Str * 3)
term4 = int(a_Str * 4)

print(term1 + term2 + term3 + term4)
# 1. --------------------
N = input()

sum = 0
str = N
for i in range(4):
    sum += int(str)
    str += N

print(sum)