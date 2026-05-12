T = int(input())
for t in range(T):
    str1 = input()
    str2 = input()

    print(f"#{t+1}", end=" ")
    if str1 in str2:
        print(1)
    else:
        print(0)