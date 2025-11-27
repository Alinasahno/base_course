numbers = [1, 2, 3, 4, 5]

if len(numbers) == 0:
    average = 0
else:
    total_sum = sum(numbers)
    average = total_sum / len(numbers)

print(f"Массив: {numbers}")
print(f"Среднее арифметическое: {average}")