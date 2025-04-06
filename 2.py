import math 
# Используется исключительно для вычисления логарифма, так как вычислять его без подключения библиотеки не разумно!

def addition() -> float|int:
    a = input('Слагаемое 1: ')
    b = input('Слагаемое 2: ')
    if a.lstrip('-').isdigit():
         a = int(a)
    elif a.replace('.','', 1).lstrip('-').isdigit():
         a = float(a)
    if b.lstrip('-').isdigit():
         b = int(b)
    elif b.replace('.','', 1).lstrip('-').isdigit():
         b = float(b)
    if isinstance(a, str) or isinstance(b, str):
            raise ValueError("Введены НЕ числа!")
    return (f'>>> {a+b}\n-------------------------')

def subtraction() -> float|int:
    a = input('Уменьшаемое: ')
    b = input('Вычитаемое: ')
    if a.lstrip('-').isdigit():
         a = int(a)
    elif a.replace('.','', 1).lstrip('-').isdigit():
         a = float(a)
    if b.lstrip('-').isdigit():
         b = int(b)
    elif b.replace('.','', 1).lstrip('-').isdigit():
         b = float(b)
    if isinstance(a, str) or isinstance(b, str):
            raise ValueError("Введены НЕ числа!")
    return (f'>>> {a-b}\n-------------------------')

def multiplication() -> float|int:
    a = input('Множитель 1: ')
    b = input('Множитель 2: ')
    if a.lstrip('-').isdigit():
         a = int(a)
    elif a.replace('.','', 1).lstrip('-').isdigit():
         a = float(a)
    if b.lstrip('-').isdigit():
         b = int(b)
    elif b.replace('.','', 1).lstrip('-').isdigit():
         b = float(b)
    if isinstance(a, str) or isinstance(b, str):
            raise ValueError("Введены НЕ числа!")
    return(f'>>> {a*b}\n-------------------------')

def division() -> float:
    while True:
        parameter = input('Выберите вид деления: Деление нацело(1); Деление с остатком(2); Обыкновенное деление(3): ')
        if parameter != '1' and parameter != '2' and parameter != '3':
                print('Введено недопустимое значение! Введите одно из предложенных значений!')
        else: break

    a = input('Делимое: ')
    b = input('Делитель: ')

    if a.lstrip('-').isdigit():
         a = int(a)
    elif a.replace('.','', 1).lstrip('-').isdigit():
         a = float(a)

    if b.lstrip('-').isdigit():
         b = int(b)
    elif b.replace('.','', 1).lstrip('-').isdigit():
         b = float(b)

    if isinstance(a, str) or isinstance(b, str):
            raise ValueError("Введены НЕ числа!")
    elif b == 0:
            raise ZeroDivisionError('Ошибка! Деление на ноль невозможно!')
    
    if parameter == '1':
        return(f'>>> {a // b}\n-------------------------')
    elif parameter == '2':
        return(f'>>> {a % b}\n-------------------------')
    elif parameter == '3':
        return(f'>>> {a / b}\n-------------------------')
    
def factorial() -> int:
    a = input('Основание: ')

    if a.lstrip('-').isdigit():
         a = int(a)
    elif a.replace('.','', 1).lstrip('-').isdigit():
         a = float(a)

    if isinstance(a, str):
            raise ValueError("Введено нецелое основание факториала или оно НЕ число!")
    elif a < 0:
            raise ValueError("Основание факториала меньше нуля!")
    fact = 1
    for i in range(1, a+1):
        fact = fact * i
    return(f'>>> {fact}\n-------------------------')

def degree() -> float|int:
    a = input('Основание: ')
    b = input('Показатель: ')

    if a.lstrip('-').isdigit():
         a = int(a)
    elif a.replace('.','', 1).lstrip('-').isdigit():
         a = float(a)

    if b.lstrip('-').isdigit():
         b = int(b)
    elif b.replace('.','', 1).lstrip('-').isdigit():
         b = float(b)

    if isinstance(a, str) or isinstance(b, str):
            raise ValueError("Введены НЕ числа!")
    
    return(f'>>> {a ** b}\n-------------------------')

def logarithm() -> float|int:
    a = input('Основание логарифма: ')
    b = input('Логарифм числа: ')

    if a.lstrip('-').isdigit():
         a = int(a)
    elif a.replace('.','', 1).lstrip('-').isdigit():
         a = float(a)

    if b.lstrip('-').isdigit():
         b = int(b)
    elif b.replace('.','', 1).lstrip('-').isdigit():
         b = float(b)

    if isinstance(a, str) or isinstance(b, str):
            raise ValueError("Введены НЕ числа!")
    elif a<=0 or a==1:
         raise ValueError('Ошибка! Основание логарифма должно быть больше нуля и не равно 1!')
    elif b<=0:
         raise ValueError('Ошибка! Брать логарифм нуля или отрицательного числа бессмысленно!')

    return(f'>>> {math.log(b)/math.log(a)}\n-------------------------')

def square_root() -> float|int:
    a = input('Подкоренное выражение: ')

    if a.lstrip('-').isdigit():
         a = int(a)
    elif a.replace('.','', 1).lstrip('-').isdigit():
         a = float(a)

    if isinstance(a, str):
            raise ValueError("Введено НЕ число!")
    elif a<0:
            raise ValueError('Ошибка! Арифметический квадратный корень извлекается строго из неотрицательных чисел! Для получения комплексных чисел используйте степень с нецелым показателем!')

    return(f'>>> {a ** 0.5}\n-------------------------"')

while True:
    print('Доступные операции:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Возведение в степень\n6. Факториал\n7. Логарифм\n8. Арифметический квадратный корень\nexit (Завершение работы)\n-------------------------')
    operation = input('Операция: ')
    if operation == 'exit':
        break
    elif operation == '1':
        print(addition())
    elif operation == '2':
        print(subtraction())
    elif operation == '3':
        print(multiplication())
    elif operation == '4':
        print(division())
    elif operation == '5':
        print(degree())
    elif operation == '6':
        print(factorial())
    elif operation == '7':
        print(logarithm())
    elif operation == '8':
        print(square_root())
    else:
        raise ValueError('Ошибка! Неизвестная операция!')

