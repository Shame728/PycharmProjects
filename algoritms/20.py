spisok = [int(i) for i in open('nums').read().split(',')]
min_num = 10 ** 10
for i in range(len(spisok)):
    if i % 2 == 1:
        if spisok[i] <= min_num:
            min_num = spisok[i]
print(min_num)