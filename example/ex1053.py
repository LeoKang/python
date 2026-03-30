message = '나는야 전역 변수'
print(message)

def no_secret():
    message = '이러면 또 지역변수'
    print(message)

no_secret()
print(message)