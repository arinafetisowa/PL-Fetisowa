import math
x = -2.235 * 10 ** -2
y = 2.23
z = 15.221
s = (math.exp(math.fabs(x - y)) * math.fabs(x - y) ** (x + y)) / (math.atan(x) + math.atan(z)) + math.pow(x,
                                                                                                          6) + math.log(
    y) ** 2
print(f"Результат вычисления: {s:.4f}")
#Округляем до 4х знаков после запятой с помощью f


