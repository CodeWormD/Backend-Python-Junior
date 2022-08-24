# алгоритм Застёжка-молния 
n = int(input('введите число '))
a = list(map(int, input('введите числа через пробел: ').split()))
b = list(map(int, input('введите числа через пробел: ').split()))
c = []
for i in range(n):
    c = list(zip(a,b))
print(*c)
#    c.append(a[1]) 
#    c.append(b[i])
# for i in c:
#     print(i, end=' ')
