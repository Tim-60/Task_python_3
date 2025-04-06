def multiplication(numbers: list[int | str], koefficient: int = 2) -> list[int | str]:
    y = []
    for i in range(len(numbers)):
             y.append(numbers[i] * koefficient)
    return (y)

lambda_multiplication = lambda numbers, koefficient = 2: list(map(lambda number: number * koefficient, numbers))

s = input('Введите числа через пробел: ')
array = [int(x) if x.isdigit() else str(x) for x in s.split() ]
print (array)

k = input('Введите множитель (по умолчанию 2): ')
if k.isdigit() == False:
    k = 2
    print('Введено некорректное значение множителя, было применено значение по умолчанию!')
elif k != '':
    k = int(k)

try:
    print(f"Результат (функция): {multiplication(array, k)}")
    print(f"Результат (лямбда-функция): {lambda_multiplication(array, k)}")
except:
    print(f"Результат (функция): {multiplication(array)}")
    print(f"Результат (лямбда-функция): {lambda_multiplication(array)}")