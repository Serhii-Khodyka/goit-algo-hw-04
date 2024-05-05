
import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генеруємо великий масив даних
data = [random.randint(0, 20000) for _ in range(10000)]

# Тестуємо сортування злиттям
time_merge = timeit.timeit(lambda: merge_sort(data.copy()), number=1)

# Тестуємо сортування вставками
time_insertion = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)

# Тестуємо Timsort (вбудована функція sorted)
time_timsort = timeit.timeit(lambda: sorted(data.copy()), number=1)

print(f"Час сортування злиттям: {time_merge} сек.") #в десять разів оціночно повільніше Timsort
print(f"Час сортування вставками: {time_insertion} сек.") #дуже повільний по результатам тестів
print(f"Час Timsort: {time_timsort} сек.") #по тестам показує найменший час, необхідний для сортування
