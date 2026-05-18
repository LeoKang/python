def solution(money):
    return list(divmod(money, 5500))

def solution(money):
    return money//5500 , money%5500

# 1. ------------------------

def solution(money):
    answer = []
    acup = 5500

    numcup = money // acup
    answer.append(numcup)
    answer.append(money % acup)
    
    return answer

money1 = 5500
print(solution(money1))

money2 = 15000
print(solution(money2))