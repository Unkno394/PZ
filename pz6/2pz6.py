# Дан список A размера N. Сформировать новый список B того же размера, элементы
# которого определяются следующим образом:
# BK = 2*AK, если AK < 5,
# AK/2 в противном случае.

import random

def print_list(lst, elements_per_line=10):
    for i in range(0, len(lst), elements_per_line):
        print(*lst[i:i + elements_per_line])

def main():
    try:
        N = int(input("Введите размер списка N: "))
        if N <= 0:
            print("Размер списка должен быть положительным")
            return
        A = [random.randint(1, 10) for _ in range(N)]
        
        print(f"\nИсходный список A: {A}")
        B = []
        for element in A:
            if element < 5:
                B.append(2 * element)
            else:
                B.append(element / 2)
        
        print("\nПолученный список B:")
        print_list(B)
        
    except ValueError:
        print("Ошибка: введите целое число!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()