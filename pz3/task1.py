while True:
    try:
        n = int(input("Введите N: "))
        if n < 0:
            print("Ошибка: отрицательное число")
            continue
        fact = 1
        i = 1
        while i <= n:
            fact = fact * i
            i = i + 1
            
        print(f"{n}! = {fact}")
        
    except:
        print("Ошибка ввода")