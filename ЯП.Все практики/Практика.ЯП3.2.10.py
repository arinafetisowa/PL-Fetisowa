k = float(input("Введите значение k: "))
c = float(input("Введите значение c: "))
if k < 5 and c > 4:
    B = k + c**2
elif k > c and k > 3:
    B = c**2 + 2
else:
    B = c - 1
print(f"Значение B: {B}")
#f-позволяет вставлять значение переменных непосредственно в строку
