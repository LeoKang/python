T = int(input())
for t in range(T):
    inp = input()

    lst = list(inp)
    lst.append('@')
    j = 0

    while True:
        remove = False
        if lst[j] == lst[j+1]:
            del lst[j:j+2]
            remove = True
        elif lst[j+1] == '@':
            break
        if j < len(lst) and remove == False:
            j += 1
        else:
            if j != 0:
                j -= 1 

    cnt = 0
    for i in lst:
        if i != '@':
            cnt += 1
    
    print(f"#{t+1} {cnt}")
