numbers = []
for i in range(3):
    num = int(input(f"Введите целое число {i + 1}: "))
    numbers.append(num)
filtered_numbers = [num for num in numbers if 1 <= num <= 3]
print("Числа в интервале [1, 3]:", filtered_numbers)

