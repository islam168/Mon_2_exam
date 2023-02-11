from random import randint

# 1.(5 баллов) Написать функцию div_by_5, принимающую 1 аргумент — число от 0 до 1000
# (проверять входные данные не нужно), и возвращающую True, если оно делится на 5 без остатка, и False - иначе.

def div_by_5(number: int) -> bool:
    if number % 5 == 0:
        res = True
    else:
        res = False

    return res


result = div_by_5(16)
print(result)


# 2. (15 баллов) Напишите функцию которая называется explore_list, которая
# принимает в качестве аргумента список из чисел (проверять, что он состоит из чисел НЕ нужно)
# и возвращает словарь, у которого должна быть следующая структура:
# {
#     ‘less_that_15’: # список элементов, которые меньше 15,
#     ‘middle’: # средний элемент в списке по индексу (без сортировки),
#     ‘odd’: # список из всех нечетных элементов в списке,
#     ‘even’: # список из всех четных элементов в списке
# }

def explore_list(num_list: list) -> dict:
    less_that_15 = []
    middle = 0
    odd = []
    even = []
    middle_list_index = num_list[len(num_list) // 2]
    for i, v in enumerate(num_list):
        if v < 15:
            less_that_15.append(v)
        if v % 2 != 0:
            odd.append(v)
        else:
            even.append(v)

        if v == middle_list_index:
            middle = v

    num_dict = {
        'less_that_15': less_that_15,
        'middle': middle,
        'odd': odd,
        'even': even
    }

    return num_dict


number_list = [1, 15, 6, 20, 35]
result = explore_list(number_list)
print(result)

# 3. (20 баллов) Напишите функцию id_generator, которая должна сгенерировать набор числовых данных длиной
# в 16 символов из целочисленных значений и вернуть в качестве строкового значения


def id_generator() -> str:
    number = ''
    for i in range(16):
        n = randint(0, 9)
        number += str(n)

    return number


print(id_generator())



# 4. (15 баллов) Напишите функцию factorial, которая будет получать
# в качестве аргумента число и ВОЗВРАЩАТЬ факториал этого числа.

def factorial(num: int) -> int:
    res = 1
    for i in range(1, num+1):

        res *= i
    return res


result = factorial(5)
print(result)


# 5. (10 баллов) Создайте функцию, которая называется my_color, данная функция принимает
# в качестве аргумента строковое значение. Полученное значение функция должна записать
# в файл, который будет называться my_color.txt. (Каждая следующая запись должна перезаписывать предыдущие записи)
def my_color(color: str) -> str:
    with open('my_color.txt', 'w',  encoding='utf-8') as file:
        file.write(color)

    with open('my_color.txt', 'r',  encoding='utf-8') as file:
        res = file.read()

    return res


result = my_color('красный')
print(result)

# 6. (15 баллов) Создать функцию get_car, которая описывает автомобиль.
# Данная функция принимает в себя два обязательных аргумента и далее ПРОИЗВОЛЬНЫЙ НАБОР
# ИМЕННОВАННЫХ АРГУМЕНТОВ **kwargs. Обязательные аргументы это brand (марка машины) и year (год выпуска).
# Далее из всех полученных аргументов функция должна построить словарь, содержащий все свойства
# автомобиля, переданные в качестве аргументов

def get_car(brand, year, **info):
    car_info = {
        'brand': brand,
        'year': year,
    }
    for key, value in info.items():
        car_info[key] = value

    return car_info


print(get_car(brand='Toyota', year=2018, color='white', fuel='diesel'))



# 7. (20 баллов) Создать функцию maskify, которая заменяет все символы, кроме последних четырех, на «#».
#     Например
#     "4556364607935616”     -->     "############5616"
#      "64607935616"          -->          "#######5616"
#                "1"              -->    "1"
#                 "4321"              -->    "4321"

def maskify(num: str) -> str:
    res = ''
    len_num = len(num)
    if len_num < 4:
        return num
    else:
        for i in range(len_num-4):
            res += '#'

        res += num[-4:]

    return res


res = maskify('4556364607935616')
print(res)
