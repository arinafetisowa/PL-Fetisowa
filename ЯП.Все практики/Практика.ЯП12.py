import tkinter as tk
from tkinter import *
from tkinter import scrolledtext
import requests


def take_json():
    entry = input_var.get()
    # код для парсинга скопирован из 12 пр добавлена проверка на ввод нужного варианта и того что вводится число от 1-100
    if entry == '8':
        # Имя пользователя github
        username = "ansible"
        # url для запроса
        url = f"https://api.github.com/users/{username}"
        # делаем запрос и возвращаем json
        user_data = requests.get(url).json()
        # довольно распечатать данные JSON
        output_json = user_data
        # фильтруем только нужные нам данные(указанные в конце практики)
        filtered_json = {'company': f'{output_json['company']}', 'created_at': f'{output_json['created_at']}',
                         'email': f'{output_json['email']}', 'id': f'{output_json['id']}',
                         'name': f'{output_json['name']}', 'url': f'{output_json['url']}'}
        window_with_text.delete(1.0, tk.END)
        window_with_text.insert(1.0, f'{filtered_json}')
    elif entry not in [str(i) for i in range(1, 101)]:
        window_with_text.delete(1.0, tk.END)
        window_with_text.insert(1.0, 'Введите только число соответствующее номеру вашего варианта.')
    else:
        window_with_text.delete(1.0, tk.END)
        window_with_text.insert(1.0, 'Вы вводите не тот номер варианта.')

    # главное окно

window = tk.Tk()
window.title('Pl-Fetisowa')
window.geometry('450x210')
window.resizable(height=False, width=False)
# виджеты которые расположены в окне
label = Label(window, text='Введите номер своего варианта:')
label.grid(row=1, column=1, sticky='W')
input_var = Entry(window, width=5)
input_var.grid(row=2, column=1, sticky='W')
button = Button(window, text='Парсить', command=take_json)
button.grid(row=1, column=2, sticky='W')
window_with_text = scrolledtext.ScrolledText(window, width=45, height=10)
window_with_text.grid(row=3, column=1)
# постоянный запуск окна
window.mainloop()