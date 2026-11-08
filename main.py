import math
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