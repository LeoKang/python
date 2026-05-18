def solution(price):
    rate = 0.8 if price >= 500000 else 0.9 if price >= 300000 else 0.95 if price >= 100000 else 1
    return int(price * rate)

# 3. ----------------------------------------

def solution(price):
    if 100000 <= price < 300000:
        return int(price * 0.95)
    elif 300000 <= price < 500000:
        return int(price * 0.90)
    elif price >= 500000:
        return int(price * 0.80)
    else:
        return int(price)

# 2. ---------------------------------------

def solution(price):
    if price >= 500000: return int(price*0.8)
    if price >= 300000: return int(price*0.9)
    if price >= 100000: return int(price*0.95)
    return price

# 1. ------------------------------------

def solution(price):
    print(price)

    if price>=100000:
        price = int(price - (price *0.05))
    elif price >= 300000:
        price = int(price - (price *0.1))
    elif price>=500000:
        price = int(price - (price *0.2))

    # if price>=500000:
    #     price = int(price - (price *0.2))
    # elif price>=300000:
    #     price = int(price - (price *0.1))
    # elif price>=100000:
    #     price = int(price - (price *0.05))

    answer = price
    return answer

price1 = 150000
print(solution(price1))

price2 = 580000
print(solution(price2))