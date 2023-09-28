# 2. Використовуючи інструкції if/else та/або if/elif/else та оператори порівняння(>, <, <=, >=. ==, !=) створити:

## a. ситуацію коли перша умова є істиною
a = 17
b = 28

if a < b:
    print('a < b')
elif a > b:
    print('a > b')
elif a == b:
    print('a == b')

## b. інструкція переходить до else
c = 24
d = 10

if c < d:
    print('c < d')
elif c == d:
    print('c == d')
else:
    print('c > d')

## c. перевірку чи число не нуль щоб при подальшому діленні на нього не виникло помилки.
e = 0

if e != 0:
    print('e != 0')
else:
    print('do not divide by zero not to have a mistake appears in further')


## d. перевірити чи дві змінні дорівнюють одна одній
f = 37
g = 37

if f == g:
    print('f == g')
else:
    print('f != g')


## e. перевірити чи дві змінні не дорівнюють одна одній
h = 19
i = 43

if h != i:
    print('h != i')

## f. креатив :)
j = 74
k = 92

if j > k:
    print('j > k')
elif (j == k or k > 50) and k % 4 == 0:
    print('j')
