number = input("Введите двузначное число: ")
if len(number) == 2 and number.isdigit():
    if number[0] == number[1]:
        print("Да")
    else:
        print("Нет")
else:
    print("Пожалуйста, введите корректное двузначное число.")
