from ctypes import Union


set = {1, 2, 3, 4, 5, 5, 6, 7, 6}


# создать неизменяемое множество
new_frozenset = frozenset({'set', 22, 55, 2, 3, 5})

# объединить два множества
together = new_frozenset | set

# одинаковые элементы в двух множествах
find = new_frozenset & set


print(set)
print(new_frozenset)
print(together)
print(find)