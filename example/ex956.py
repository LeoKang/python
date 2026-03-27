def get_price(is_vip=False):
    if is_vip == True:
        return 10000
    else:
        return 15000

price1 = get_price(True)
print(price1)
price2 = get_price()
print(price2)
price3 = get_price()
print(price3)
price4 = get_price()
print(price4)