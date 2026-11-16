import math
#a)
try:
    num = float(input("Enter a number: "))
    kor = math.sqrt(num)

    if kor ** 2 == num:
        print("Число является полным квадратом")
    else:
        raise ValueError('Число не является полным квадратом')
except ValueError as e:
    print(f"Исключение: {e}")
#б)
try:
    n = input()
    spisok = [i for i in n]
    if spisok == spisok[::-1]:
        print('Строка является полиндромом')
    else:
        raise ValueError('Число не является полиндромом')
except ValueError as e:
    print(f'Исключение: {e}')
#в)
try:
    num = float(input())
    root = math.sqrt(num)
    assert root ** 2 == num, print('Число не является полным квадратом')
    print('Число является полным квадратом')
except AssertionError as e:
    print(e)