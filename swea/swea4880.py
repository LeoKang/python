def get_winner(p1, p2, cards):
    c1 = cards[p1 - 1]
    c2 = cards[p2 - 1]
    
    win_cases = {1: 3, 2: 1, 3: 2}
    
    if c1 == c2:
        return p1 if p1 < p2 else p2
    elif win_cases[c1] == c2:
        return p1
    else:
        return p2

def divide(i, j, cards):
    if i == j:
        return i
    
    mid = (i + j) // 2
    
    left_winner = divide(i, mid, cards)
    right_winner = divide(mid + 1, j, cards)
    
    return get_winner(left_winner, right_winner, cards)

T_str = input()
if T_str:
    T = int(T_str)
    for tc in range(1, T + 1):
        N = int(input())
        cards = list(map(int, input().split()))
        
        result = divide(1, N, cards)
        
        print(f"#{tc} {result}")