#Задача 1 Дано трехзначное число. Проверить истинность высказывания: «Цифры данного числа образуют возрастающую или убывающую последовательность».
try:
    num = int(input("Введите трёхзначное число: "))
    if not 100 <= num <= 999:
        print("Ошибка: число должно быть трёхзначным!")
        exit()
except ValueError:
    print("Ошибка: введите целое число!")
    exit()

digits = [int(d) for d in str(num)]

is_ascending = digits[0] < digits[1] < digits[2]
is_descending = digits[0] > digits[1] > digits[2]

if is_ascending or is_descending:
    print("Истинно: цифры образуют возрастающую или убывающую последовательность.")
else:
    print("Ложно: цифры не образуют монотонную последовательность.")