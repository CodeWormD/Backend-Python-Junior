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


def minimum(list):
    los = list[0]
    for b in list:
        if b < los:
            los = b
    print(los)

# minimum([-3, 2, 3, 11, 22, -2, -100, -2233])

def shortest_word(s):
    b = s.split()
    l = b[0]
    for i in b:
        if len(i) < len(l):
            l = i
    print(len(l))

# shortest_word('bitcoin take over the world maybe who knows perhaps')


def solution(number):
    summ = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
    print(summ)

# solution(4)
# print(6 % 3)


def maskify(data):
    datalen = len(data)
    last = list(data[-4:])
    pas = datalen - 4
    s = []
    if datalen > 4:
        for i in range(pas):
            i = '#'
            s.append(i)
        return ''.join(s + last)
    else:
        return data

# maskify('yH>qMSVZmt#VfBbV7$X`tu9$D')



def listinlist(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            print(False)
    print(True)

# listinlist('ABCDEFGHIJKLMNOPQRSTUV12313,,,WXYZ')



def printer_error(s):
    alph = 'abcdefghijklm'
    total = len(s)
    errors = 0
    for i in s:
        if i not in alph:
            errors += 1
    print(f'{errors}/{total}')


# printer_error('kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu')


def digital_root(n):
    while n>9:
        n = sum(map(int,str(n)))
    print(n)

# digital_root(493193)


def is_isogram(string):
    l = []
    for char in string.lower():
        l.append(char)
    if len(l) > len(set(l)):
        return False
    return True

# is_isogram('isogram')
# is_isogram('aba')



def elements_sum(arr, d=0):
    c = 0
    lenn = len(arr) - 1
    for i in arr:
        if len(i) < 3 and d == 0:
            c += 0
            d = 0
        elif len(i) != 0:
            c += i[lenn]
            lenn -= 1
    print(c+d)


# elements_sum([[-12, 326, -188, -42, -351, -7, -37, 4, 9, -67, 0, -309, 721, -561, -886, 477, 0, 48], [18, 4, -22, 10, -1, -10, -816, 318, 93, 127, -34, -514, -77, 14], [-82, -1, -6, -8, 80, -76], [992, 189, -815, -425, 89, -69, 80, -4, 5, -27, -4, -77, -2, 1, -109, -75, 24, -1, 92, 6, -174, -3, 635, -1, -62, -8, -935, -882, -734], [-458, 246, -13, -1, 99, 6, 23, 2, 631, -31, -69, 9, 693, 0, 1, -723, 10, 9, -77, -8, 67, -367, -587, 693, 41, -303, 47, -6, 755, 25, -1, -723, 628, 346, 87, -453, -995, -61], [68, -439, 197, -724, -45, 25, 19, 1], [1, -33, 81, -295, 82, 181, -551, -517, -8, 995, -116, -298, -7, -16, -1, -69, -51, 15, 5, -79, -119, -333, -32, -50, -34], [10, -5, 0, -710, -826, -1, -739, -413, 550, -94, -49, -100, 76, 10, 336, -324, -8, -62, 207, 1, 4, 5, -24, -468, -24, -19, -488, 7, 72, -543, 984], [0], [-411, 771, -42, -769, 816, 320, 9, -52, -390, -763, -68, 12], [-541, 1, -5, -60, -10, 0, -624, -308, -1], [774, -81, 16, 92, -446, -10, -45, -159, -453, 47, -205, 6, 0, 546, 15, 5, 24, 143, 395, -204, -54, -6, 8, 855, -19, -582, 820], [-36, 978, 130, -6, 0, 76, 726, -1, -9, 0, -428, 595, 87, 485, 901, 540, 41, 84, -230, 351, 642, -318, -880, 8, 1, -85, 9, 2, 62, -83, 1, 95, -8, -9], [49, -1], [-81, 784, 370, 717, -93, 948, 1, 661, 33, 905, 107, 3, -300, -16, -424, 0, -371, 5, -845, 6, -69, 330, -882, -76, -845, 99, -25, 0, -5, -229, -814, 40, 244, -4, 56, 9, 851, 0, -446], [-559, 60, 5, -12, -10, -295, -890, -7, 0, -8, -49, 6, 809, 30, 353, -864, -971, 40, 43, 950, 14, -91, 1, 0, 133, -984, 331, -2, 65, 86, -6, -70, -79, -55], [-63, -768, -470, 0, 98, -456, 7, 0, 56, -385, -65, 0, 82, -9, -516, 261, 965, -7, -32, -4, 362, 599, -657, 62, -977, 985, 8, 858, -992, 95, 610, -250], [1, 0, 99, -1, -235, -469, -525, -170, -59, 61, 568, 761, -53, 188, -564, 84, -676, 0, -432, 9, 419, 77, 6, 17, 5, -188, -98, -47, 476, -8, -5, 6, 212, 8], [-18, 76, -900, 99, 64, -36, 74, -119, 4, -5, 23, -62, -98, 424, 1, -57], [-7, -320, -79, 980, 21, -420, 44, 482, -977, 490, -83, 2, 0, 85, -33, -73, 62, 884, 116, 10, -4, -788, -10, 43, -326, 10, -947, 475, 699, -17], [-9, 94, -3, -54, 4, 0, 4, 32, 480, 507, 67, 63, -952, 0, -765, 3, 69, 24, 85, 585, 768, 9, 484, 3, 992, 578, -1], [-353, -395, -578, 60, -100, -21, -1, 61, 0, -960, 6, -81, 8, -40, 49, 0, -94, -695, -77, -133, -197, -906, 846, -69, -3, -31, -99, -97, 395, -699, 947, 45, 172, -737, -106, 370, -37, 467], [1, 487, 1, 24, 507]])




def fibs_fizz_buzz(n):
    l = []
    new = []
    fib1 = 1
    fib2 = 1
    l.append(fib1)
    l.append(fib2)
    if n <= 1:
        return [1]
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        l.append(fib1 and fib2)
    for b in l:
        if b % 5 == 0 and b % 3 == 0:
            b = 'FizzBuzz'
        elif b % 3 == 0:
            b = 'Fizz'
        elif b % 5 == 0:
            b = 'Buzz'
        new.append(b)
    print(new)
# fibs_fizz_buzz(1)


def check_test(signature, n):
    if n == 0:
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    else:
        return None


def tribonacci(signature, n):
    q, w, e = signature[0], signature[1], signature[2]
    l = [q, w, e]
    check_err = check_test(signature, n)
    if check_err == None:
        for b in range(3, n):
            q, w, e = w, e, q+w+e
            l.append(e)
        print(l)
    else:
        print(check_err)


# tribonacci([0, 0, 1], 10)




def order(sentence):
    num = [i for i in '123456789']
    new = sentence.split()
    di = {}
    c = []
    for i in new:
        for b in i:
            if b in num:
                a = int(b)
                di[a] = i
    for key in sorted(di):
        c.append(di[key])
    print(' '.join(c))

order("is2 Thi1s T4est 3a")
order("4of Fo1r pe6ople g3ood th5e the2")