N, B = input().split()
B = int(B)

num_dict = {str(i): i for i in range(10)}
num_dict.update({chr(i + 55): i for i in range(10, 36)})

total = 0
square = len(N) - 1

index = 0
while index < len(N):
    total += num_dict[N[index]] * (B ** square)
    index += 1
    square -= 1
# 3. -----------------------------------
A = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']

N , B = input().split()
b = int(B)
n = len(N)
s = 0
for i in N:
    I = A.index(i)
    s += I*(b**(n-1))
    n -= 1
print(s)
# 2. ----------------------------
print(int('A', 11))

# n, b = input().split()
# print(int(n, int(b)))
# 1. -------------------------------------------------
# N, B = input().split()

# res = 0
# for idx, ch in enumerate(N):
#     if ch.isdigit():
#         res += int(ch) * (int(B) ** (len(N) - 1 - idx))
#     else:
#         res += (ord(ch) - 55) * (int(B) ** (len(N) - 1 - idx))
# print(res) 
