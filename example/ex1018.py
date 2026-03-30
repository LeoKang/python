def secret():
    message = '이건 나만의 비밀'
    print(message)
    message = '함수 내에서는 자유롭게 수정이 가능해요'

def please():
    message = '이렇게 하면 되지?'
    print(message)

message2 = '이것도 비밀'
print(message2)
secret()
please()