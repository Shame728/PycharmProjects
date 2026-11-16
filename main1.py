import random
from functools import reduce
#28
#в
# import random
# from functools import reduce
# spisok = [random.randint(-100, 100) for x in range(5)]
# mult = reduce(lambda x, y: x * y, spisok)
# print(mult)
#29
#a
# spisok = [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8]
# res = list(map(lambda x: 1 if x > 0 else (0 if x == 0 else -1), spisok))
# result = [round(res.count(0) / len(spisok), 2), round(res.count(1) / len(spisok), 2), round(res.count(-1) / len(spisok),2)]
# print(result)
#b
# spisok = [random.randint(-10, 10) for x in range(5)]
# res = list(filter(lambda x: x < 0, spisok))
# print(res)
# sp = reduce(lambda x, y: x * y, res)
# print(sp)
