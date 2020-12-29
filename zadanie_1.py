#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Основная ветка программы, не считая заголовков функций, состоит из двух строки кода. Это вызов функции test() и
# инструкции if __name__ == '__main__' . В ней запрашивается на ввод целое число. Если оно положительное,
# то вызывается функция positive(), тело которой содержит команду вывода на экран слова "Положительное". Если число
# отрицательное, то вызывается функция negative(), ее тело содержит выражение вывода на экран слова "Отрицательное”.

def test(A):
    if A >= 0:
        positive()
    elif A < 0:
        negative()


def positive():
    print('Положительное')


def negative():
    print('Отрицательное')


if __name__ == '__main__':
    a = int(input('Введите целое число: '))
    test(a)