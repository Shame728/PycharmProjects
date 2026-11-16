from collections import *
from enum import Enum
#a)
spisok = [1, 1, 1, 2, 2, 2, 2, 4, 4, 4]
spisok.sort()
counter = Counter(spisok)
min_count = min(counter.values())
for elem in spisok:
    if counter[elem] == min_count:
        print(elem)
        break
#b)
def cities(spisok):
    result = defaultdict(list)
    for name, populations in spisok:
        if populations < 100000:
            key = 'Меньше 100 тыс'
        elif populations < 1000000:
            key = 'Меньше 1 М'
        else:
            key = 'Больше 1 М'
        result[key].append(name)
    return result

spisok = [("Город A", 80_000),
    ("Город B", 500_000),
    ("Город C", 1_200_000),
    ("Город D", 150_000),
    ("Город E", 800_000)]
print(cities(spisok))
#c)
class Animals(Enum):
    dog = 15
    cat = 5
    rabbit = 2

Animals = Enum('Animals', [('dog', 15), ('cat', 5), ('rabbit', 2)])
print(Animals.cat.value)
print(Animals.rabbit.value)
print(Animals.dog.value)
#d)
def keys(dict_list):
    return frozenset(key for d in dict_list for key in d)
data = [
    {'name': 'Alice', 'age': 25},
    {'age': 30, 'city': 'New York'},
    {'city': 'Paris', 'job': 'Engineer'}

]
unique_keys = keys(data)
print(unique_keys)
#e)
from collections import namedtuple

Book = namedtuple('Book', ['title', 'author', 'pages'])

def filter_books(books_list, min_pages):
    return [book for book in books_list if book.pages > min_pages]

library = [
    Book("Властелин колец", "Дж. Р. Р. Толкин", 1200),
    Book("Маленький принц", "Антуан де Сент-Экзюпери", 96),
    Book("1984", "Джордж Оруэлл", 328),
    Book("Преступление и наказание", "Фёдор Достоевский", 600)
]

thick_books = filter_books(library, 400)
for book in thick_books:
    print(f"{book.title} — {book.pages} стр.")
#f)
d = OrderedDict()
d['a'] = 1
d['b'] = 2
d['c'] = 3

def f(dict):
    data = OrderedDict((k, v) for k, v in dict.items() if v > 2 )
    return data
print(f(d))
