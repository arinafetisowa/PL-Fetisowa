#cумма и произведение элементов списка
spisok = list(map(int, input("вводим числа через пробел: ").split()))
#map - строки в целые числа
#list - преобразуем в список целых чисел
#нахождение суммы и произведения
summa = sum(spisok)
proizv = 1
for chisl in spisok:
    proizv *= chisl
    #продолжаем умножать все числа в списке
print("сумма элементов списка:", summa)
print("произведение элементов списка:", proizv)

