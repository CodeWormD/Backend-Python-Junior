list = [1, 2, 3, 3, 4, 5]

# добавляем елемент в конец списка
list.append('new element')

# добавляем елемент int на место с индексом
list[1] = 22

# добавляем новый елемент типа лист в конец списка
list.append(['a', 'b', 'c'])

# добавляем елемент кортеж на место с индексом
list[-3] = ('кортеж', 'еще кортеж')

# получить элемент по индексу
get_element = list[5]

# удалить элемент
list.remove(22)

# количество елементов в списке со значением 3
result = list.count(3)

# длинна списка
result2 = len(list)

# print(list)
# print(get_element)
# print(result)
# print(result2)


# поменять места значения
a = 'stroke'
b = 100
a, b = b, a


# проверка списка на дубликаты
listr = [1, 1, 1, 2, 3, 3, 4, 5, 6]
first = len(listr)
second = len(set(listr))

print(first, second)



