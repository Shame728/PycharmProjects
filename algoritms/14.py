def calc(x, y, op):
    if op == 1:
        return x - y
    elif op == 2:
        return x * y
    elif op == 3:
        return x / y
    else:
        return x + y
x = float(input("Введите первое число: "))
y = float(input("Введите второе число: "))
op = int(input('Введите тип операции: 1 - "-", 2 - "*", 3 - "/", 4 - "+"'))
print(calc(x, y, op))