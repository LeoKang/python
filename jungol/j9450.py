def line(n=4):
    if n == 0:        
        print()       
        return
    print('=', end='')
    line(n - 1)

line()
print("line 함수를 호출하였습니다.")
print("line 함수를 다시 호출합니다.")
line()

# 4. -------------------------
# def draw_line():
#     print ('='*25)

# draw_line()
# print('Line함수를 호출하였습니다.')
# print('line함수를 호출합니다.')
# draw_line()

# # 3. --------------------------

# def m_f():
#     print('''=========================
# line 함수를 호출하였습니다.
# line 함수를 다시 호출합니다.
# =========================''')
# m_f()

# # 2. ----------------------------------
# def line():
#     print('='*25)
#     print('line 함수를 호출하였습니다.')
#     print('line 함수를 다시 호출합니다.')
#     print('='*25)
# line()
# line()
# # 1. -------------------------------
# def draw_line():
#     print("="*25)

# draw_line()
# print("line 함수를 호출하였습니다.")
# print("line 함수를 다시 호출합니다.")
# draw_line()