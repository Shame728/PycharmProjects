def calc(vir):
    numbers = {
        'ноль': 0, 'один': 1, 'два': 2, 'три': 3,
        'четыре': 4, 'пять': 5, 'шесть': 6, 'семь': 7,
        'восемь': 8, 'девять': 9, 'десять': 10,
        'одиннадцать': 11, 'двенадцать': 12, 'тринадцать': 13,
        'четырнадцать': 14, 'пятнадцать': 15, 'шестнадцать': 16,
        'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19,
        'двадцать': 20, 'тридцать': 30, 'сорок': 40,
        'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70,
        'восемьдесят': 80, 'девяносто': 90
    }

    words = {value: key for key, value in numbers.items()}

    spisok = vir.split()
    calculate = []
    i = 0

    while i < len(spisok):
        if spisok[i] == 'скобка':
            if spisok[i + 1] == 'открывается':
                calculate.append('(')
            else:
                calculate.append(')')
            i += 2
            continue

        elif spisok[i] == 'умножить':
            calculate.append('*')
            i += 2
            continue

        elif spisok[i] == 'разделить':
            calculate.append('/')
            i += 2
            continue

        elif spisok[i] == 'плюс':
            calculate.append('+')
        elif spisok[i] == 'минус':
            if i == 0 or calculate[-1] in ['+', '-', '*', '/', '(', 'NEG']:
                calculate.append('NEG')
            else:
                calculate.append('-')

        elif spisok[i] in numbers:
            value = numbers[spisok[i]]

            if value >= 20 and value % 10 == 0:
                if spisok[i + 1] in numbers:
                    next_value = numbers[spisok[i + 1]]
                    value += next_value
                    i += 1

            calculate.append(value)

        i += 1

    vir = []
    operations = []
    priority = {'+': 1, '-': 1, '*': 2, '/': 2, 'NEG': 3}

    for nums in calculate:
        if isinstance(nums, int):
            vir.append(nums)

        elif nums == '(':
            operations.append(nums)

        elif nums == ')':
            while operations and operations[-1] != '(':
                vir.append(operations.pop())

            operations.pop()

        else:
            while (operations and operations[-1] != '(' and priority[operations[-1]] >= priority[nums]):
                vir.append(operations.pop())

            operations.append(nums)

    while operations:
        vir.append(operations.pop())

    stack = []

    for nums in vir:
        if isinstance(nums, int):
            stack.append(nums)

        elif nums == 'NEG':
            stack.append(-stack.pop())

        else:
            num2 = stack.pop()
            num1 = stack.pop()

            if nums == '+':
                stack.append(num1 + num2)
            elif nums == '-':
                stack.append(num1 - num2)
            elif nums == '*':
                stack.append(num1 * num2)
            elif nums == '/':
                stack.append(num1 / num2)

    result = stack[0]

    if result < 0:
        return 'минус ' + calc_number(-result, words)

    if result == int(result):
        return calc_number(int(result), words)

    return result


def calc_number(number, words):
    if number in words:
        return words[number]

    if number < 100:
        tens = number // 10 * 10
        units = number % 10

        if units == 0:
            return words[tens]

        return words[tens] + ' ' + words[units]

    return str(number)


play = True
while play:
    vir = input('Введите выражение: ')
    try:
        print(calc(vir))
    except Exception:
        print('Error')
    print('Для выхода введите q')
    if vir == 'q':
        flag = input('Вы уверены (y/n)')
        if flag == 'n':
            pass
        else:
            play = False

