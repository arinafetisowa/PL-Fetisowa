#В массиве действительных чисел все нулевые элементы заменить на среднее арифметическое всех элементов массива.
spisok = list(map(float, input("введём числа через пробел: ").split()))
#float - в действительные чтсла
sredneearifm = sum(spisok) / len(spisok) if spisok else 0  #избегая деления на 0
#нашли среднее арифметическое
spisok = [sredneearifm if x == 0 else x for x in spisok] #меняем нулевые на среднее арифметическое
print("массив после замены:", spisok)
