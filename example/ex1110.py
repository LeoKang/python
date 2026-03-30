f = open('list.txt', 'r', encoding='utf8')
for line in f:
    print(line, end='')
f.close()