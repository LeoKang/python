list = ["가위", "바위", "보"]
man1 = input().strip()
man2 = input().strip()

if man1 == man2:
    print("Result : Draw")
else:
    list1 = list.index(man1)
    list2 = list.index(man2)

    if (list1 - list2) % 3 == 1:
        print("Result : Man1 Win!")
    else:
        print("Result : Man2 Win!")

# 2. -------------------------------
# L = ['가위','바위','보']
# f = input()
# s = input()
# '가위' < '바위' , '바위' < '보', '보' < '가위'
# if f == s:
#     print('Result : Draw')
# elif f > s:
#     print('Result : Man1 Win!')
# else:
#     print('Resilt : Man2 Win!')

# 1. -----------------------------
# man1 = input()
# man2 = input()

# mjp = ['가위', '바위', '보']
# win = -1

# if man1==mjp[0]:
#     if man2==mjp[1]:
#         win = 2
#     elif man2==mjp[2]:
#         win = 1
#     else:
#         win = 0
# elif man1==mjp[1]:
#     if man2==mjp[0]:
#         win = 1
#     elif man2==mjp[2]:
#         win = 2
#     else:
#         win = 0
# elif man1==mjp[2]:
#     if man2==mjp[0]:
#         win = 2
#     elif man2==mjp[1]:
#         win = 1
#     else:
#         win = 0

# if win!=0:
#     print(f"Result : Man{win} Win!")
# else:
#     print(f"Result : Draw")