def TrianglePS(a):
    try:
        perimeter = 3 * a
        
        # Площадь равностороннего треугольника: S = (a² * √3) / 4
        area = (a * a * (3 ** 0.5)) / 4
        return perimeter, area
    except Exception as e:
        raise ValueError(f"Ошибка вычисления: {e}")

def calculate_triangles():
    try:
        while True:
            try:
                print("\nВведите длины сторон трех равносторонних треугольников:")
                triangles_data = []
                for i in range(3):
                    while True:
                        try:
                            side_input = input(f"Длина стороны треугольника {i+1}: ")
                            side = float(side_input)
                            
                            if side <= 0:
                                print("Ошибка: длина стороны должна быть положительной!")
                                continue
                                
                            if side > 1000000:
                                print("Ошибка: слишком большая длина стороны!")
                                continue
                                
                            triangles_data.append(side)
                            break
                            
                        except ValueError:
                            print("Ошибка: введите числовое значение!")
                        except KeyboardInterrupt:
                            print("\n\nВыход из программы...")
                            return
                        except Exception as e:
                            print(f"Неожиданная ошибка: {e}")
                print("РЕЗУЛЬТАТЫ:")              
                for i, side in enumerate(triangles_data, 1):
                    try:
                        perimeter, area = TrianglePS(side)
                        print(f"Треугольник {i}:")
                        print(f"  Сторона: {side}")
                        print(f"  Периметр: {perimeter:.2f}")
                        print(f"  Площадь: {area:.2f}")
                        print()
                    except Exception as e:
                        print(f"Ошибка при расчете треугольника {i}: {e}")
                
                print("что-то вводите дальше или нажмите Ctrl+C для выхода")
                
            except KeyboardInterrupt:
                print("\n\nВыход из программы...")
                break
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
                
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")


# Запуск второй задачи
print("\n=== ЗАДАЧА 2: Расчет треугольников ===")
print("выход Ctrl+C")
calculate_triangles()