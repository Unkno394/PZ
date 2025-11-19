def even_numbers_up_to(n):
	try:
		n_int = int(n)
	except Exception:
		raise ValueError("Параметр n должен быть числом")

	if n_int < 2:
		return []
	count = n_int // 2
	evens = []
	i = 1
	while i <= count:
		evens.append(2 * i)
		i += 1
	return evens


if __name__ == '__main__':
	try:
		while True:
			try:
				s = input('\nВведите целое число ')
				n = int(s)
				result = even_numbers_up_to(n)
				if not result:
					print("Нет чётных чисел в диапазоне.")
				else:
					print('Чётные числа от 2 до', n, ':')
					print(' '.join(str(x) for x in result))
			except ValueError:
				print("Ошибка: введите целое число.")
				break
	except KeyboardInterrupt:
		print('\nПрограмма завершена.')

