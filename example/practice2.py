lang = 'PYTHON'
print(lang)
print(lang[0])
print(lang[-1])
print(lang[:3])
print(lang[2:])
print(lang[:])

num = 3
num += 2 # num = num + 2
print(num)

num -= 1
num *= 2
num /= 4
print(num)

snack = '꿀꽈배기'
print(len(snack))

snack = '''꿀꽈배기는
너무
맛있어요'''
print(snack)

print('-' * 10)
print('NadoCoding')
print('*' * 20)

letter = 'how are YOU?'
print(letter.lower())
print(letter.upper())
print(letter.capitalize())
print(letter.title())
print(letter.swapcase())
print(letter.split())

str1 = letter.split()
print(str1[0].capitalize())
print(str1[1].capitalize())
print(str1[2].capitalize())

letter = "how are YOU?"
print(letter.count('how'))

letter = "how are you?"
print(letter.count('o'))

s = '나도고등학교'
print(s.startswith('나도'))
print(s.endswith('초등학교'))
print(s.endswith('고등학교'))

s2 = '...나도고등학교...'
print(s2.strip('.'))

s3 = '.,.나도고등학교.,.'
print(s3.strip('.'))

s4 = '나도고등학교'
print(s4.replace('고등학교', '고교'))

s5 = '나도고교너도고교'
print(s5.replace('고교', '고등학교'))

s = '나도고등학교'
print(s.find('학교'))
print(s.find('너도'))
print(s.center(10, '-'))