def second_largest(chiselki, largest=0, second=0):
    if not chiselki:  #tсли список пуст,возвращаем второй по величине
        return second
    pervi = chiselki[0]
#присвоили сюда первый элемент списка
    if pervi == 0:  #завершение ввода, если текущее число - 0
        return second

    #для определения второго по величине элемента
    if largest is 0 or pervi > largest:
        second = largest  #обновляем второго бро по величине
        largest = pervi
    elif pervi != largest and (second is 0 or pervi > second):
        second = pervi

    #вызов для следующего числа
    return second_largest(chiselki[1:], largest, second)
chiselki = []
print("Введите натуральные числа (0 для завершения):")
while True:
    chis = int(input())
    if chis == 0:
        break
    chiselki.append(chis)

result = second_largest(chiselki)
if result is not 0:
    print(f"Второй по величине элемент: {result}")
else:
    print("Недостаточно уникальных элементов для определения второго по величине.")