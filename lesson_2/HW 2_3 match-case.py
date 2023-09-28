# 3. Використовуючи інструкції match-case створити структуру для привітання різних користувачів в залежності від їх імені.

name = 'Vladyslav'

match name:
    case 'Iryna':
        print('Hello!')
    case 'Oleksandr':
        print('Good morning!')
    case 'Svitlana' | 'Vladyslav' | 'Igor':
        print('Hi!')
    case 'Veronika' | 'Olena':
        print('Wazzup!')
    case _:
        print('I do not understand you')
