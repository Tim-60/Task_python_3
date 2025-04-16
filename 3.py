def function_name(search: str, status: bool, *args: tuple, **kwargs: dict) -> list[int] | str:
    """
Функция динамически обрабатывает аргументы, возвращая различные результаты в зависимости от значений search и status.
Некорректное значение search вызывает исключение.
Функциональность:
При search="args" и status=True: возвращает список целых чисел (list[int]), извлечённых из позиционных аргументов (*args).
При search="args" и status=False: возвращает строку (str), объединяющую все позиционные аргументы (*args).
При search="kwargs": возвращает строку (str), представляющую все именованные аргументы (**kwargs) в формате ключ-значение.
Во всех остальных случаях возникает исключение.
Аргументы:
search (str): Определяет тип обрабатываемых аргументов ("args" для позиционных, "kwargs" для именованных).
status (bool): Определяет формат вывода позиционных аргументов. Имеет значение только когда search="args".
*args (tuple): Позиционные аргументы.
**kwargs (dict): Именованные аргументы.
Возвращает:
list[int]: Список целых чисел, извлечённых из *args (при search="args" и status == True).
str: Строка, представляющая либо объединённые *args (при search="args" и status == False), либо пары ключ-значение для **kwargs (при search="kwargs").
None: В случае возникновения исключения.
Исключения:
        ValueError: Если search не равно "args" или "kwargs".
    """
    result: list[int] = []
    result_2: str = ""
    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return result_2
    else:
        raise ValueError("Error for search")
