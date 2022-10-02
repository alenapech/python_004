# 1. Вычислить число c заданной точностью d
# Пример: при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$
import math
d = list(input('Введите точность округления: ').split('.'))
r = len(d[1])
p = float(input('Введите число: '))
print("Результат: %s" % round(p, r))


# 2. Задайте натуральное число N. Напишите программу, которая 
# составит список простых множителей числа N.
n = int(input('Введите натуральное число: '))
i = 2
while n > 1:
    while n % i == 0:
        print(i, end=' ')
        n = n/i
    i += 1

# 3. Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной 
# последовательности.
l = list(map(int, input('Введите последовательность (через пробел): ').split())) #вводить через пробел
print(l)
print(list(dict.fromkeys(l)))

# 4. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать
# в файл многочлен степени k.
# Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
k = int(input('Введите степень многочлена: '))
ress = []
for i in range(k+1):
    res = ''
    q = random.randint(0, 100)        
    if (q != 0):
        s = k-i
        res += str(q)
        if (s != 0):
            res += '*x^'+str(s)
    ress.append(res)
ress = list(filter(("").__ne__, ress))
result  = ' + '.join(map(str,ress)) + " = 0"
print(result)
with open('result.txt', 'w') as f:
    f.write(result)

# 5. Даны два файла, в каждом из которых находится запись 
# многочлена. Задача - сформировать файл, содержащий сумму 
# многочленов.
import re

def get_dict(source):
    sdict = {}
    for x in source:
        m = re.findall("x\^\d$", x)
        for y in re.findall("^\d*", x):
            u = y
        if (len(m) == 0):
            sdict['none'] = int(u)
        for t in m:
            sdict[t] = int(u)
    return sdict

with open('result.txt', 'r') as f1:
    s1 = f1.read()
with open('result2.txt', 'r') as f2:
    s2 = f2.read()
s1 = s1.replace(' = 0', '')
s2 = s2.replace(' = 0', '')
s1 = s1.split(sep=' + ')
s2 = s2.split(sep=' + ')
sdict1 = get_dict(s1)
sdict2 = get_dict(s2)
print(sdict1)
print(sdict2)
for dk in sdict2.keys():
    if(sdict1.keys().__contains__(dk)):
        sdict2[dk] += sdict1[dk]
ress = []
for dk in sdict2.keys():
    p = ""
    if (dk != "none"):
        p = "*" + str(dk)
    ress.append(str(sdict2[dk]) + p)
print(' + '.join(map(str,ress)) + " = 0")