N=int(input())

for _ in range(N):
    OXshow=list(input())
    Q=0
    coin=0
    for i in range(len(OXshow)):
        if OXshow[i] == "O" :
            coin+=1
        else:
            coin=0
        Q+=coin
    print(Q)
# 2. ---------------------------------
T = int(input())

for i in range(T):
    ox_res = input()
    total_score = 0
    current_line = 0
    
    for char in ox_res:
        match char:
            case 'O':
                current_line += 1
                total_score += current_line
            case 'X':
                current_line = 0
            case _:
                pass
    print(total_score)

# 1. ---------------------------
T = int(input())
for x in range(T):
    str = input()   # OOXXOXXOOO
    # print(str)

    sum = 0
    score = 1
    for i in str:
        # print(i, end=' ')
        if i=='O':
            sum += score
            score += 1
        else:
            score = 1
    print(sum)
