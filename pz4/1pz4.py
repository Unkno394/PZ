#Даны целые положительные числа N и K. Найти сумму 1K + 2К + ... + NK

while True:
    try:
        n = int(input("Введите целое положительное число N: "))
        k = int(input("Введите целое положительное число K: "))
        
        if n <= 0 or k <= 0:
            print("Ошибка: числа должны быть положительными!")
            continue
            
        total_sum = 0
        for i in range(1, n + 1):
            power_result = i ** k
            total_sum += power_result
        
        print(f"Результат: 1^{k} + 2^{k} + ... + {n}^{k} = {total_sum}")
        break
        
    except ValueError:
        print("Ошибка: введите целые числа!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
