def ask(word):
    code = ord(str(word))
    if 65 <= code <= 90:
        return '대문자'
    elif 97 <= code <= 122:
        return '소문자'

TC = int(input())

for i in range(1, TC + 1):
    alpha = input()
    S = ask(alpha)
    print(f'#{i} {alpha} 는 {S} 입니다.')
# 4. ---------------------------------------------
res = ""
T = int(input())
for test_case in range(1, T + 1):
    E = input()
    B = ord(E)
    if 97 <= B <= 122:
        res += f"#{test_case} {E} 는 소문자 입니다.\n"
    elif 65 <= B <= 90:
        res += f"#{test_case} {E} 는 대문자 입니다.\n"
    else:
        res += f"#{test_case} {E} 는 알파벳이 아닙니다.\n"
print(res)
# 3. -------------------------------------------
N = int(input())

up = [chr(i) for i in range(0x41, 0x5B)]
low = [chr(j) for j in range(0x61, 0x7B)]

# print(up)
# print(low)

for x in range(N):
    alphabet = input()
    if alphabet in up:
        print(f'#{x+1} {alphabet} 는 대문자 입니다.')
    elif alphabet in low:
        print(f'#{x+1} {alphabet} 는 소문자 입니다.')
# 2. ----------------------------------------
N=int(input())
list1 = [
    'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
    'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l',
    'z', 'x', 'c', 'v', 'b', 'n', 'm'
]
j=1
while True:
    try:
        i = input()
        if not i :
            break
        if i in list1:
            print(f"#{j} {i} 는 소문자 입니다.")
            j+=1
    except EOFError:
        break

# 1. --------------------------------
T = int(input())
for test_case in range(1, T + 1):
    ch = input()
    if ch.islower():
        print(f"#{test_case} {ch} 는 소문자 입니다.")
    else:
        print(f"#{test_case} {ch} 는 대문자 입니다.")
