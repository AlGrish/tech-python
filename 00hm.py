# -*- coding: utf-8 -*-

import sys

if sys.version_info[0] == 2:
    input = raw_input
else:
    input = input

a1 = input('В каком году закончится поддержка Python 2?\nВаш ответ: ')

if a1 == str('2020'):
    print('Это правильный ответ!')
else:
    print('К сожалению, неверно.')

a2 = input('Всё в Python - \nОтвет: ')

if a2 == str('объект'):
    print('Это правильный ответ!')
else:
    print('К сожалению, неверно.')

a3 = input('Какие циклы бывают в Python?\nОтвет: ')

if a3 == str('for, while') or str('while, for') or str('for') or str('while'):
    print('Это правильный ответ!')
else:
    print('К сожалению, неверно.')

a4 = input('Как называется универсальная кодировка?\nОтвет: ')

if a4 == str('Unicode'):
    print('Это правильный ответ!')
else:
    print('К сожалению, неверно.')

print('На сегодня это всё :-)')
