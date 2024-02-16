from random import randint

7# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код.


LOWER_LIMIT = 0
UPPER_LIMIT = 1000
num = randint(LOWER_LIMIT, UPPER_LIMIT)
count = 0
print("Угадайте число.")
while count < 10:
    count += 1
    num_win = int(input(f"Попытка {count} из 10. Введите число: "))
    if (num_win == num):
        print("Вы угадали число!")
        break
    elif (num_win > num):
        print("Загаданное число меньше")
    elif (num_win < num):
        print("Загаданное число больше")
    if (count == 10):
        print("Попытки закончились")