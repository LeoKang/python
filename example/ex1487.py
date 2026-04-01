num1 = 10
num2 = 0

try:
    result = num1 / num2
    print(f'연산 결과는 {result}입니다.')
except Exception as err:
    print('에러가 발생했어요 : ', err)
except ZeroDivisionError:
    print('0으로 나눌 수 없어요.')
except TypeError:
    print('값의 형태가 이상해요')

