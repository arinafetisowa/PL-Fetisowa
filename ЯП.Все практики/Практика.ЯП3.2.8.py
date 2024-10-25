x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
if x < 2:
    B = x * y + 1
elif x > y:
    B = y**2 + x**3
else:
    B = x**2 + 2
print(f"Значение B: {B}")
