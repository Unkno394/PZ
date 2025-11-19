def draw_horizontal_line(length, symbol='*'):
    print(symbol * length)


def draw_vertical_line(height, width, symbol='*'):
    for _ in range(height):
        print(symbol + ' ' * (width - 2) + symbol)


def create_word_frame():
    try:
        while True:
            try:
                word = input("Введите слово для рамки: ")

                if not word.strip():
                    print("Ошибка: слово не может быть пустым!")
                    continue
                
                symbol = input("Введите символ для рамки (по умолчанию '*'): ").strip()
                if not symbol:
                    symbol = '*'
                elif len(symbol) != 1:
                    print("Ошибка: нужно ввести ровно один символ!")
                    continue
                
                frame_length = len(word) + 4
        
                if frame_length > 100:
                    print("Ошибка: слишком длинное слово!")
                    continue
                
                print()

                draw_horizontal_line(frame_length, symbol)

                print(f"{symbol} {word} {symbol}")

                draw_horizontal_line(frame_length, symbol)
                
                print() 
                
            except KeyboardInterrupt:
                print("\n\nВыход из программы...")
                break
            except Exception as e:
                print(f"Неожиданная ошибка: {e}")
                
    except KeyboardInterrupt:
        print("\nПрограмма завершена.")

print("выход Ctrl+C")
print()
create_word_frame()