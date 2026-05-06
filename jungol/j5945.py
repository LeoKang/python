n = int(input())
n_sum = 1

if 1 <= n <= 50 and n % 2 == 1:
    for i in range(1, n + 1):
        lst = []

        for j in range(1, i + 1):
            lst.append(n_sum)
            n_sum += 1

        if i % 2 == 0:
            print(*lst[::-1])
        else:
            print(*lst)
else:
    print('INPUT ERROR!')
    
# 2. -------------------------------

try:
    n = int(input())
    # print(n)
    if 1 <= n <= 50 and n % 2 == 1:
        curr = 1
        for i in range(1, n + 1):
            row = [curr + j for j in range(i)]
            curr += i
            
            display = row if i % 2 != 0 else row[::-1]
            print(" ".join(map(str, display)))
    else:
        print("INPUT ERROR!")
except:
    print("INPUT ERROR!")

# 1. ----------------------------------

n = int(input())
# print(n)

if (n<1 or n>50) or (n % 2 == 0):
    print("INPUT ERROR!")
else:
    # n-row n-col
    lst = [[0 for j in range(n)] for i in range(n)]

    num = 1
    for i in range(n):
        for j in range(i+1):
            lst[i][j] = num
            num += 1

    for i in range(len(lst)):  # 세로 길이
        if i % 2 != 0:
            lst[i].reverse()

    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] != 0:
                print(lst[i][j], end=' ')
        print()