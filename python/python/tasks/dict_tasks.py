from typing import Dict

dict = {
    'Masha': 21,
    'Sasha': 32,
    'Diana': 44,
    'Misha': 10
}

# Добавить новое значение в словарь
dict['New name'] = 33
dict[(1, 2, 3)] = [11, 22, 33]

# Удалить элемент по ключу
dict.pop('Sasha', 'No item')
del dict['Misha']

# Удалить последний элемент в словаре
a = dict.popitem()


# проход по словарю
def dict_road(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


# print(dict)
# print(dict['Masha'])
# print(dict.get('Masha', 'No key'))
# print(dict.keys())
# print(dir(dict))
# dict_road(**dict)