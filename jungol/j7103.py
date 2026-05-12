A = []
for i in range(5):
    A.append(int(input()))

B = A
print("A: ", A)
print("B: ", B)
A.reverse()
print("A: ", A)
print("B: ", B)


# 4. ----------------------------------

# lst = []
# lst2 = []
# lst3 = []

# for i in range(8):
#     a = int(input())
#     lst.append(a)
#     lst2 = lst[0:5]
#     lst3 = list(reversed(lst2))
    
# print(lst3)
# print(lst)
# print(lst2)

# # 2. --------------------------------

# A = [int(input()) for _ in range(5)]
# B = A[:]
# C = A[::-1]
# print(C)

# B.extend([int(input()) for _ in range(3)])
# print(B)
# print(A)

# # 1. -----------------------------

# A = []
# for i in range(5):
#     A.append(int(input()))

B = A.copy()
# C = A.copy()
# C.reverse()

# for i in range(3):
#     B.append(int(input()))

# print(C)
# print(B)
# print(A)

# # print("C: ", C)
# # print("B: ", B)
# # print("A: ", A)
