# Дано множество A из N точек (точки заданы своими координатами x, у). Среди всех
# точек этого множества, лежащих в первой или третьей четверти, найти точку,
# наиболее близкую к началу координат. Если таких точек нет, то вывести точку с
# нулевыми координатами.
# Расстояние R между точками с координатами (x1, y1) и (x2, у2) вычисляется по формуле:
# R = √(x2 – x1)2 + (у2 – y1)2
# .
# Для хранения данных о каждом наборе точек следует использовать по два списка: первый
# список для хранения абсцисс, второй — для хранения ординат.


import math
import random

def main():
    try:
        N = int(input("Введите количество точек N: "))
        if N <= 0:
            print("Количество точек должно быть положительным числом!")
            return
        
        x_coords = [round(random.uniform(-10, 10), 2) for _ in range(N)]
        y_coords = [round(random.uniform(-10, 10), 2) for _ in range(N)]
        
        print("\nКоординаты точек:")
        print("X:", x_coords)
        print("Y:", y_coords)
        min_distance = float('inf')
        closest_point_index = -1
        point_found = False
        
        for i in range(N):
            x, y = x_coords[i], y_coords[i]
        
            if (x > 0 and y > 0) or (x < 0 and y < 0):
                distance = math.sqrt(x**2 + y**2)  # R = √(x² + y²)
                
                if distance < min_distance:
                    min_distance = distance
                    closest_point_index = i
                    point_found = True
        
        print("\nРезультат поиска:")
        if point_found:
            x, y = x_coords[closest_point_index], y_coords[closest_point_index]
            print(f"Найдена ближайшая точка в 1-й или 3-й четверти:")
            print(f"Координаты: ({x}, {y})")
            print(f"Расстояние до начала координат: {min_distance:.2f}")
        else:
            print("Точек в 1-й или 3-й четверти не найдено")
            print("Возвращаем точку с нулевыми координатами: (0, 0)")
            
    except ValueError:
        print("Ошибка: введите целое число!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    main()

    