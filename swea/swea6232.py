str1 = str(input())
str2 =''.join(reversed(str1))
if str1 == str2:
    print(str1,"\n입력하신 단어는 회문(Palindrome)입니다."

# 4. ------------------------------------
INT = input()

if INT == INT[::-1]:
    print(f"{INT}\n입력하신 단어는 회문(Palindrome)입니다.")
# 3. -----------------------------
# INT = input()
# Q_INT = INT[::-1]

# res=[]

# for i in range(len(INT)) :
#     if INT[i] == Q_INT[i]:
#         res.append(True)

# if len(res) == len(INT):
#     print(f"{INT} \n입력하신 단어는 회문(Palindrome)입니다.")
# else : 
#     print(f"{INT} \n입력하신 단어는 회문(Palindrome)이 아닙니다.")
# # 1. -----------------------
# from jungol.j9701 import p

# inp = input()
# # print(inp)

# s = 0
# e = len(inp)-1

# isPalindrome = True
# while isPalindrome:
#     if s == e:
#         break
#     elif inp[s] == inp[e]:
#         isPalindrome = True
#     else:
#         isPalindrome = False
#     s += 1
#     e -= 1

# print(inp)
# if isPalindrome==True:
#     print(f"입력하신 단어는 회문(Palindrome)입니다.")
