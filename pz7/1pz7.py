def calculate_expression():
    try:
        expression = input("Введите арифметическое выражение (например, '4+7-2-8'): ").strip()
        result = 0
        current_number = ""
        operation = '+'
        
        for char in expression:
            if char.isdigit():
                current_number += char
            elif char in '+-':
                if current_number:
                    if operation == '+':
                        result += int(current_number)
                    else:
                        result -= int(current_number)
                    current_number = ""
                operation = char
        
        if current_number:
            if operation == '+':
                result += int(current_number)
            else:
                result -= int(current_number)
        
    except ValueError:
        print("Ошибка: некорректное число в выражении")
if __name__ == "__main__":
    calculate_expression()