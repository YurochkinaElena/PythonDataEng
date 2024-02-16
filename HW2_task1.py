# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

from fractions import Fraction
HEX = 16

num: int = int(input('Введите число: '))
test_num: int = num
result: str = ''
while test_num > 0:
    numHex = test_num % HEX
    if numHex < 10:
        result = str(numHex) + result
    else:
        result = chr(97 + numHex - 10) + result
        # result = "abcdef"[numHex - 10] + result
    test_num //= HEX
print(f'For {HEX} {result =}')
print(f'{hex(num)   =}')