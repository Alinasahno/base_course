import random

N = 10

a1 = [random.randint(0, 100) for _ in range(N)]
a2 = [random.randint(0, 100) for _ in range(N)]
a3 = [random.randint(0, 100) for _ in range(N)]

print("Массив1:", a1)
print("Массив2:", a2)
print("Массив3:", a3)

max_el = max(max(a1), max(a2), max(a3))

total_sum = sum(a1) + sum(a2) + sum(a3)

print(f"\nНаибольший элемент среди всех массивов: {max_el}")
print(f"Сумма всех элементов массивов: {total_sum}")