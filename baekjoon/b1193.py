# n = int(input())
# f = 1  # 층수
# m = 0  # 대빵
# while m+f < n:
#     m += f
#     f += 1
# l = n-m
# if f % 2 == 0: #짝수 층(왼-오)
#     x = l
#     y = f-l+1
# else:         #홀수 층(오-왼)
#     x = f-l+1
#     y = l
# print(f"{x}/{y}")
# # 3. ----------------------------------
# X = int(input())
# diagonal = 1
# while X > diagonal:
#     X -= diagonal
#     diagonal += 1

# # [홀수일 때 결과, 짝수일 때 결과]를 리스트에 미리 담아둠
# # 홀수(diagonal%2==1): 분자 감소(diagonal-X+1), 분모 증가(X)
# # 짝수(diagonal%2==0): 분자 증가(X), 분모 감소(diagonal-X+1)
# results = [
#     (X, diagonal - X + 1),          # diagonal이 짝수일 때 (index 0)
#     (diagonal - X + 1, X)           # diagonal이 홀수일 때 (index 1)
# ]

# # diagonal % 2 결과에 따라 튜플을 선택하고 언패킹 출력
# up, down = results[diagonal % 2]
# print(f"{up}/{down}")
# # 2. --------------------------
# a = int(input())  
# group = 1

# while a > group: 
#    a -= group 
#    group += 1

# if group % 2 == 0:   
#    bunja = a
#    bunmo = group - a + 1
# else: 
#    bunja = group - a + 1
#    bunmo = a

# print(f"{bunja}/{bunmo}")

# 1. -----------------------------------------------------
X = int(input())
# right(1) -> left-down(1) -> down(1) -> right-up(2) ->
# right(1) -> left-down(3) -> down(1) -> right-up(4) ->
# right(1) -> left-down(5) -> down(1) -> right-up(6) ->
# right     => b += 1
# left-down => a += 1, b -= 1
# down      => a += 1
# right-up  => a -= 1, b += 1
# a / b
# 1   1
# 1   2
# 2   1
# 3   1
# 2   2
# 
a = 1
b = 1
start = 1
dir = 1 # 1 : right, 2 : left-down, 3 : down, 4 : right-up
cnt_ld = 1 # left-down
cnt_ru = 2 # right-up
cnt = 0
while start < X:
    print(f"{dir}::{a}/{b}")
    match dir:
        case 1:     # right
            b += 1
            dir += 1
            cnt = 0 # 방향 전환
        case 2:     # left-down
            cnt += 1
            a += 1
            b -= 1
            if(cnt <= cnt_ld):
                dir += 1
                cnt_ld += 2
                cnt = 0
        case 3:     # down
            a += 1
            dir += 1
            cnt = 0
        case 4:     # right-up
            cnt += 1
            a -= 1
            b += 1
            if(cnt <= cnt_ru+1):
                dir = 1
                cnt_ru += 2
    print(f"{start}-{dir}:::{a}/{b}")    
    start += 1

print(f"{a}/{b}")
