import requests
import os


def solve_quadratic_equation(a, b, c):
    '''Задание «Квадратное уравнение», тема «Функции»
    '''
    D = b ** 2 - 4 * a * c
    if D < 0:
        return 'Корней нет'
    elif D == 0:
        x = -b / (2 * a)
        return round(x, 2)
    else:
        x1 = (-b + D ** 0.5) / 2 * a
        x2 = (-b - D ** 0.5) / 2 * a
        return round(x1, 2), round(x2, 2)

def collect_unique_names(names):
    '''Задание «Соберите уникальные имена преподавателей», тема «Множества»
    '''
    nested_lists = all([isinstance(element, list) for element in names])
    if nested_lists:
        names = sum(names, [])
    all_unique_names = ', '.join(sorted({name.split()[0] for name in names}))
    return all_unique_names

def get_initials(initials):
    '''Задание «ФИО», тема «Введение в типы данных»
    '''
    initials = ''.join([name[0] for name in initials])
    return initials

def create_yadisk_folder():
    '''Функция создания папки на ЯДиске
    '''
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    params = {
        'path': 'Folder for testing',
        'fields': 'name'
    }
    headers = {
        'Authorization': f'OAuth {os.getenv('YADISKTOKEN')}'
    }
    response = requests.put(url, params=params, headers=headers)
    return response
