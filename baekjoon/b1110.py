N = int(input())
anonym = [N // 10, N % 10]
start = list(anonym)
count = 0

while True:
    count += 1
    
    new_box = (anonym[0] + anonym[1]) % 10
    anonym[0], anonym[1] = anonym[1], new_box
    
    if anonym == start:
        break
print(count)
# 2. ------------------------------
N = input()
start = int(N)
num = int(N)
count = 0
while True:
    a = num % 10
    b = num // 10
    num = a*10 + (a+b)%10
    count += 1
    if num == start:
        break
print(count)
# 1. ------------------------------
N = input()
# print(N)

num = int(N)
cnt = 0
while True:
    a = num // 10
    b = num % 10
    new = a + b
    newStr = str(b) + str(new % 10)
    # print(newStr)
    num = int(newStr)
    cnt = cnt + 1
    if num == int(N) and cnt != 0:
        break;

print(cnt)
