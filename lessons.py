import random
from enum import Enum
import math
from functools import reduce
from math import sqrt
from collections import Counter, defaultdict, OrderedDict
import string
from modules import *
import re
import operator

# data = {
#     'a':1, 'b':2, 'c':3
# }
# print(data)
# key = input('Введите ключ, который нужно удалить')
# del data[key]
# print(data)
#
#
# def remove_space_in_key(dic):
#     return {key.replace(' ', ''): value for key, value in dic.items()}
# data = {
#     ' a ':1, ' b ':2, ' c ':3
# }
# print(data)
# print(remove_space_in_key(data))
#
# data = {'a': [1, 2], 'b': [3, 4]}
# res = [{key:v} for key, value in data.items() for v in value]
# print(res)
#12
# data = tuple(i for i in random.sample(range(1,100), 10))
# print(data)
# elem = int(input('Введите число, которое нужно удалить: '))
# if elem not in data:
#     print('Нет такого элемента')
# data = tuple(i for i in data if i != elem)
# print(data)
#
# tuples_data = (
#     tuple(i for i in random.sample(range(1,100), 5)),
#     tuple(i for i in random.sample(range(1,100), 5)),
#     tuple(i for i in random.sample(range(1,100), 5)),
# )
# nums = []
# print(tuples_data)
# for i in tuples_data:
#     i = tuple(j for j in i if j > 5)
#     summa = 0
#     for j in i:
#         summa += j
#     nums.append(summa / len(i))
# print(nums)
#13
# nums = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# num = (input('Введите число: '))
# for i in num:
#     if int(i) in nums:
#         nums.remove(int(i))
# print(nums)
# st_a = {1, 2, 3, 4, 5, 6}
# st_b = {4, 5, 7}
# flag = True
# for i in st_b:
#     if flag:
#         if i not in st_a:
#             flag = False
#         else:
#             flag = True
#     else:
#         print(False)
#         break
# print(flag)
# 14
# def calc(x, y, op):
#     if op == 1:
#         return x - y
#     elif op == 2:
#         return x * y
#     elif op == 3:
#         return x / y
#     else:
#         return x + y
# x = float(input("Введите первое число: "))
# y = float(input("Введите второе число: "))
# op = int(input('Введите тип операции: 1 - "-", 2 - "*", 3 - "/", 4 - "+"'))
# print(calc(x, y, op))

#15
# alf = string.ascii_uppercase + string.ascii_lowercase + string.digits + '_'
#
# def IsIdent(s):
#     if (s == '') or ('_' not in s):
#         return False
#     for i in s:
#         if i not in alf:
#             return False
#     return True
# print(IsIdent('asdfsdfs_'))

#16
#a)
# def combine_lists(list1, list2, order='first_second'):
#     if order == 'first_second':
#         return list1 + list2
#     elif order == 'second_first':
#         return list2 + list1
#     else:
#         return 'error'
# print(combine_lists([1,2], [3,4], 'second_first'))
#b)
# def procces_string(text, sep=' '):
#     spisok = text.split(sep)
#     if sep == ' ':
#         for i in range(len(spisok)):
#             spisok[i] = spisok[i].lower()
#         res = ' '.join(spisok)
#     else:
#         for i in range(len(spisok)):
#             spisok[i] = spisok[i][0].upper() + spisok[i][1:]
#         res = f'{sep}'.join(spisok)
#     return res
# print(procces_string('python_java_c++', '_'))
#c)
# def difference(*args):
#     spisok = args[0]
#     for i in args[1:]:
#         for j in i:
#             if j in spisok:
#                 spisok.remove(j)
#     return spisok
# print(difference([1, 2, 3], [2, 3, 4], [3, 4, 5]))
#d)

# def common_in_at_least_two(*lists):
#
#     element_counts = Counter()
#     for lst in lists:
#         element_counts.update(set(lst))
#
#     return [i for i, count in element_counts.items() if count >= 2]
# print(common_in_at_least_two([1, 2], [2, 3], [2, 4]))
#17)
# def reverse_number(n, cur=0):
#     if n == 0:
#         return cur
#     return reverse_number(n // 10, cur * 10 + n % 10)
# print(reverse_number(1243))
#18)
# print(sub((1,2), (3,4)))
# print(skal((1,2), (3,4)))
# print(count((1,2), (4,6)))
# 19)
# first = open('first.txt', 'r')
# line = first.readline()
# second = open('second.txt', 'r')
# line_1 = second.readline()
# res = line + line_1
# with open('second.txt', 'w') as f:
#     f.write(res)
#20
# spisok = [int(i) for i in open('nums').read().split(',')]
# min_num = 10 ** 10
# for i in range(len(spisok)):
#     if i % 2 == 1:
#         if spisok[i] <= min_num:
#             min_num = spisok[i]
# print(min_num)
#22
#a)
# def validate_emails(email):
#     email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
#
#     if re.match(email_regex, email):
#         return True
#     return False
#
# print(validate_emails('test@example.com'))
# print(validate_emails('invalid-email@'))
# print(validate_emails(''))
#b)
# def find_all_time(file_path):
#     time_pattern = r'\b(?:[01]\d|2[0-3]):[0-5]\d\b'
#     with open(file_path, 'r') as f:
#         text = f.read()
#         times = re.findall(time_pattern, text)
#         return times
#
# print(find_all_time('time.txt'))



#23
#a)
# try:
#     num = float(input("Enter a number: "))
#     kor = math.sqrt(num)
#
#     if kor ** 2 == num:
#         print("Число является полным квадратом")
#     else:
#         raise ValueError('Число не является полным квадратом')
# except ValueError as e:
#     print(f"Исключение: {e}")
#б)
# try:
#     n = input()
#     spisok = [i for i in n]
#     if spisok == spisok[::-1]:
#         print('Строка является полиндромом')
#     else:
#         raise ValueError('Число не является полиндромом')
# except ValueError as e:
#     print(f'Исключение: {e}')
#в)
# try:
#     num = float(input())
#     root = math.sqrt(num)
#     assert root ** 2 == num, print('Число не является полным квадратом')
#     print('Число является полным квадратом')
# except AssertionError as e:
#     print(e)
#24
#a)
# spisok = [1, 1, 1, 2, 2, 2, 2, 4, 4, 4]
# spisok.sort()
# counter = Counter(spisok)
# min_count = min(counter.values())
# for elem in spisok:
#     if counter[elem] == min_count:
#         print(elem)
#         break
#b)
# def cities(spisok):
#     result = defaultdict(list)
#     for name, populations in spisok:
#         if populations < 100000:
#             key = 'Меньше 100 тыс'
#         elif populations < 1000000:
#             key = 'Меньше 1 М'
#         else:
#             key = 'Больше 1 М'
#         result[key].append(name)
#     return result
#
# spisok = [("Город A", 80_000),
#     ("Город B", 500_000),
#     ("Город C", 1_200_000),
#     ("Город D", 150_000),
#     ("Город E", 800_000)]
# print(cities(spisok))
#c)
# class Animals(Enum):
#     dog = 15
#     cat = 5
#     rabbit = 2
#
# Animals = Enum('Animals', [('dog', 15), ('cat', 5), ('rabbit', 2)])
# print(Animals.cat.value)
# print(Animals.rabbit.value)
# print(Animals.dog.value)
#d)
# def keys(dict_list):
#     return frozenset(key for d in dict_list for key in d)
# data = [
#     {'name': 'Alice', 'age': 25},
#     {'age': 30, 'city': 'New York'},
#     {'city': 'Paris', 'job': 'Engineer'}
#
# ]
# unique_keys = keys(data)
# print(unique_keys)
#e)
# from collections import namedtuple
#
# Book = namedtuple('Book', ['title', 'author', 'pages'])
#
# def filter_books(books_list, min_pages):
#     return [book for book in books_list if book.pages > min_pages]
#
# library = [
#     Book("Властелин колец", "Дж. Р. Р. Толкин", 1200),
#     Book("Маленький принц", "Антуан де Сент-Экзюпери", 96),
#     Book("1984", "Джордж Оруэлл", 328),
#     Book("Преступление и наказание", "Фёдор Достоевский", 600)
# ]
#
# thick_books = filter_books(library, 400)
# for book in thick_books:
#     print(f"{book.title} — {book.pages} стр.")
#f)
# d = OrderedDict()
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
#
# def f(dict):
#     data = OrderedDict((k, v) for k, v in dict.items() if v > 2 )
#     return data
# print(f(d))



#25

# class Triangl:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def square(self):
#         p = (self.a + self.b + self.c) / 2
#         return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
#
#     def per(self):
#         return self.a + self.b + self.c
#
# tri = Triangl(3, 4, 5)
#
# print(tri.square())
# print(tri.per())
#26
# class Salary:
#     def __init__(self, name, last_name, otch, year, zp, upper, cur_days, max_days):
#         self.name = name
#         self.last_name = last_name
#         self.otch = otch
#         self.year = year
#         self.zp = zp
#         self.upper = upper
#         self.cur_days = cur_days
#         self.max_days = max_days
#         self.sal = self.zp * self.cur_days + self.upper / 100 * (self.zp * self.cur_days)
#     def summa(self):
#         return f'{self.name} {self.last_name} заработал за месяц {self.sal}'
#     def blocked(self):
#         return f'Удержанная сумма у {self.name} {self.last_name}: {self.sal * 0.13}'
#     def givven(self):
#         return f'Выдали: {self.sal * 0.87}'
#     @property
#     def expirience(self):
#         return f'{self.name} {self.last_name} отработал: {2026 - self.year}'
#
# sal = Salary('Виталий', 'Казанцев', 'Александрович', '2008', 500000, 5, 30, 31)
# print(sal.summa())
# print(sal.blocked())
# print(sal.givven())
#27
# class Equation:
#     def __init__(self):
#         pass
#     def solve(self):
#         return 'Считаю уравнение'
#     def display(self):
#         return 'Вывожу уравнение'
#
# class LinearEq(Equation):
#     def __init__(self, a, b):
#         super().__init__()
#         self.a = a
#         self.b = b
#     def solve(self):
#         if self.a == 0:
#             return False if self.b != 0 else 'Бесконечно много решений'
#         return -self.b / self.a
#     def display(self):
#         ur = f'{self.a}x + {self.b} = 0'
#         ans = self.solve()
#         print(ur)
#         print(f'Корeнь: {ans}')
#
# class QuadraticEq(Equation):
#     def __init__(self, a, b, c):
#         super().__init__()
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def solve(self):
#         if self.a == 0:
#             return LinearEq(self.b, self.c).solve()
#         d = self.b ** 2 - 4 * (self.a * self.c)
#         if d < 0:
#             return 'Нет решений'
#         elif d == 0:
#             return [-self.b / (self.a * 2)]
#         else:
#             x1 = ((-self.b + math.sqrt(d)) / (2 * self.a))
#             x2 = ((-self.b - math.sqrt(d)) / (2 * self.a))
#             return [x1, x2]
#
#     def display(self):
#         if self.a == 0:
#             return LinearEq(self.b, self.c).display()
#         ur = f'{self.a}x ** 2 + {self.b}x + {self.c} = 0'
#         ans = self.solve()
#         print(ur)
#         print(ans)
#
#
# eq = QuadraticEq(1, -5,6)
# eq.display()
#28
#a)
# spisok = [random.randint(-100, 100) for _ in range(10)]
# sort_sp = sorted(spisok, key=lambda x: (x < 0, x))
# print(sort_sp)
#b)
# data = [
# ["яблоко", "банан", "груша"],
#     ["киви", "апельсин", "манго"],
#     ["вишня", "ананас", "слива"]
# ]
#
# sort_data = [sorted(i, key=lambda x: x) for i in data]
# for i in sort_data:
#     print(i)
#c)
# spisok = [random.randint(-100, 100) for i in range(3)]
# mult = reduce(lambda x, y: x*y, spisok)
# print(spisok)
# print(mult)
#29)
spisok = [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]
y = len(spisok)
res = map(lambda x: (x < 0, x), )