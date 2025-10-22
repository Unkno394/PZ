def draw_horizontal_line(length, symbol='*'):
    """
    Рисует горизонтальную линию из заданного количества символов.
    """
    print(symbol * length)


def draw_vertical_line(height, width, symbol='*'):
    """
    Рисует вертикальные линии по бокам.
    """
    for _ in range(height):
        print(symbol + ' ' * (width - 2) + symbol)


def create_word_frame():
    """
    Создает рамку вокруг слова с использованием горизонтальных и вертикальных линий.
    """
    try:
        while True:
            try:
                word = input("Введите слово для обрамления: ")
                
                # Проверка на пустой ввод
                if not word.strip():
                    print("Ошибка: слово не может быть пустым!")
                    continue
                
                symbol = input("Введите символ для рамки (по умолчанию '*'): ").strip()
                if not symbol:
                    symbol = '*'
                elif len(symbol) != 1:
                    print("Ошибка: нужно ввести ровно один символ!")
                    continue
                
                # Вычисляем длину рамки
                frame_length = len(word) + 4
                
                # Проверка на слишком длинную строку
                if frame_length > 100:
                    print("Ошибка: слишком длинное слово!")
                    continue
                
                print()  # Отступ для красоты
                
                # Верхняя горизонтальная линия
                draw_horizontal_line(frame_length, symbol)
                
                # Вертикальные линии с текстом
                print(f"{symbol} {word} {symbol}")
                
                # Нижняя горизонтальная линия
                draw_horizontal_line(frame_length, symbol)
                
                print()  # Пустая строка для разделения
                
            except KeyboardInterrupt:
                print("\n\nВыход из программы...")
                break
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
                
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")


# Запуск первой задачи
print("=== ЗАДАЧА 1: Рамка вокруг слова ===")
print("выход Ctrl+C")
print()
create_word_frame()