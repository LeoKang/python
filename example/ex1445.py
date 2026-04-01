num1 = 6
num2 = 0
try:
    print('num1 / num2')
    result = num1 / num2
    print(num1, '/', num2, ' = ', end=' ')
    print(result)
except Exception as err:
    print('에러가 발생했어요', err)
else:
    print('정상 동작했어요')
finally:
    print('수행종료')