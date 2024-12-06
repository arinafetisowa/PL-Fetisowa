def factorial(n):
    #здесь рекурсивно вычтем факториал
    return 1 if n <= 1 else n * factorial(n - 1)
def calculate_expression(x, n):
    #вычисляем x^n / n!
    return (x ** n) / factorial(n)
x = float(input("Введите значение x: "))
n = int(input("Введите натуральное число n: "))
result = calculate_expression(x, n)
print(f"Результат выражения {x}^{n} / {n}! = {result}")
