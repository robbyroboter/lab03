def bubble_sort(arr, ascending=True):
    n = len(arr)
    # Проходим по массиву несколько раз
    for i in range(n):
        # На каждой итерации уменьшаем количество проверяемых элементов
        for j in range(0, n - i - 1):
            # Если сортировка по возрастанию, сравниваем arr[j] > arr[j + 1]
            # Если по убыванию, сравниваем arr[j] < arr[j + 1]
            if (arr[j] > arr[j + 1] and ascending) or (arr[j] < arr[j + 1] and not ascending):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Запрашиваем количество элементов
n = int(input("Введите количество чисел: "))

# Вводим список чисел с клавиатуры
arr = []
for _ in range(n):
    num = int(input(f"Введите число {_ + 1}: "))
    arr.append(num)

# Запрашиваем направление сортировки
order = input("Введите направление сортировки (по возрастанию/по убыванию): ").strip().lower()

# Определяем направление сортировки
ascending = True
if order == "по убыванию":
    ascending = False

# Сортировка массива методом пузырька в зависимости от направления
bubble_sort(arr, ascending)

# Вывод отсортированного массива
print("Отсортированный массив:", arr)
