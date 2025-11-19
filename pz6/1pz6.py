import random

def main():
    try:
        N = int(input("Введите размер списка N: "))
        if N <= 0:
            print("Размер списка должен быть положительным")
            return
        A = []
        while len(A) < N:
            num = random.randint(1, 100)
            if num not in A:
                A.append(num)
        
        A.sort()
        
        print(f"\nИсходный список A: {A}")
        if N < 2:
            print("Разность прогрессии: 0")
            return
            
        diff = A[1] - A[0]
        is_arithmetic = True
        
        for i in range(2, N):
            if A[i] - A[i-1] != diff:
                is_arithmetic = False
                break
        
        if is_arithmetic:
            print(f"Элементы образуют арифметическую прогрессию")
            print(f"Разность прогрессии: {diff}")
        else:
            print("Элементы НЕ образуют арифметическую прогрессию")
            print("Разность прогрессии: 0")
            
    except ValueError:
        print("Ошибка: введите целое число!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()