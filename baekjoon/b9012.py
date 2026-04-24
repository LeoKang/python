# def check():
#     Str=input()

#     while "()" in Str:
#         Str = Str.replace("()","")
        
#     if len(Str) == 0:
#         print("YES")
#     else :
#         print("NO")

# N = int(input())

# for _ in range(N):
#     check()

# 2. -------------------------
# t = int(input())
# # print(t)
# for x in range(t):
#     ps = input()
#     count = 0
    
#     for char in ps:
#         if char == '(':
#             count += 1
#         else:
#             count -= 1
        
#         if count < 0:
#             break
            
#     if count == 0:
#         print("YES")
#     else:
#         print("NO")

# 1. ---------------------------
T = int(input())

for i in range(T):
    inp = input()
    lst = []
    res = True;

    for j in inp:
        print(j, end="")
        if j=="(":
            lst.append(j)
        else:
            if len(lst) != 0:
                lst.pop()
            else:
                res = False
    if len(lst)==0 and res==True:
        print("YES")
    else:
        print("NO")