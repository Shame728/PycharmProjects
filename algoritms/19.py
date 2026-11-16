
first = open('first.txt', 'r')
line = first.readline()
second = open('second.txt', 'r')
line_1 = second.readline()
res = line + line_1
with open('second.txt', 'w') as f:
    f.write(res)
    print('Теперь текст из первого файлика находится перед текстом второго')