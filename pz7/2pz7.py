def replace_all_occurrences():
    """
    Замена всех вхождений строки S1 на строку S2 в строке S
    """
    try:
        S = input("Введите основную строку S: ")
        S1 = input("Введите строку S1 для поиска: ")
        S2 = input("Введите строку S2 для замены: ")
        
        if not S1:
            print("Ошибка: строка для поиска не может быть пустой")
            return
        
        print(f"\nИсходная строка S: '{S}'")
        print(f"Строка для поиска S1: '{S1}'")
        print(f"Строка для замены S2: '{S2}'")
        
        result = S.replace(S1, S2)
        
        print(f"Результат после замены: '{result}'")
  
        count = S.count(S1)
        if count == 0:
            print("Вхождений строки S1 не найдено")
        else:
            print(f"Количество замененных вхождений: {count}")
            
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    replace_all_occurrences()