from collections import Counter
# a)
def combine(list1, list2, order='first_second'):
    if order == 'first_second':
        return list1 + list2
    elif order == 'second_first':
        return list2 + list1
    else:
        return 'Error'
print(combine([1, 2], [3, 4], 'second_first'))
#b)
def procces_string(text, sep=' '):
    spisok = text.split(sep)
    if sep == ' ':
        for i in range(len(spisok)):
            spisok[i] = spisok[i].lower()
        res = ' '.join(spisok)
    else:
        for i in range(len(spisok)):
            spisok[i] = spisok[i][0].upper() + spisok[i][1:]
        res = f'{sep}'.join(spisok)
    return res
print(procces_string('python_java_c++', '_'))
#c)
def difference(*args):
    spisok = args[0]
    for i in args[1:]:
        for j in i:
            if j in spisok:
                spisok.remove(j)
    return spisok
print(difference([1, 2, 3], [2, 3, 4], [3, 4, 5]))
#d)

def common(*lists):

    element_counts = Counter()
    for lst in lists:
        element_counts.update(set(lst))

    return [i for i, count in element_counts.items() if count >= 2]
print(common([1, 2], [2, 3], [2, 4]))