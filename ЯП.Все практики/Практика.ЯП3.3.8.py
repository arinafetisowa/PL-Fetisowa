def days_in_month(month):
    months = {
        1: ("Январь", 31),
        2: ("Февраль", 28),  # Не учитываем високосные годы для простоты
        3: ("Март", 31),
        4: ("Апрель", 30),
        5: ("Май", 31),
        6: ("Июнь", 30),
        7: ("Июль", 31),
        8: ("Август", 31),
        9: ("Сентябрь", 30),
        10: ("Октябрь", 31),
        11: ("Ноябрь", 30),
        12: ("Декабрь", 31)
    }

    return months.get(month, ("Некорректный номер месяца", None))
try:
    month_number = int(input("Введите номер месяца (1-12): "))
    month_name, days = days_in_month(month_number)
    if days is not None:
        print(f"{month_name}: {days} дней")
    else:
        print(month_name)
except ValueError:
    print("Пожалуйста, введите целое число.")
