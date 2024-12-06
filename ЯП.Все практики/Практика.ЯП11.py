from tkinter import *
from tkinter import ttk, messagebox, filedialog, scrolledtext
from tkinter.ttk import Combobox
# функции, которые срабатывают по нажатию кнопок
def calculator_task1():
    sg = input_sing.get()
    dg1 = input_digit1.get()
    dg2 = input_digit2.get()
    try:
        if sg == '+':
            answer = int(dg1) + int(dg2)
        elif sg == '-':
            answer = int(dg1) - int(dg2)
        elif sg == '*':
            answer = int(dg1) * int(dg2)
        elif sg == '/':
            answer = int(dg1) / int(dg2)
        label_with_answer.configure(text=f'={answer}')
    except ZeroDivisionError:
        label_with_answer.configure(text='=ZeroDivisionError!!!')
    except Exception as ex:
        label_with_answer.configure(text='=Input error!!!')

def radiobutton_task2():
    input_radiobutton = selector.get()
    messagebox.showinfo('Ваш выбор', f'Вариант {input_radiobutton})')

def work_with_text_task3():
    open_file = filedialog.askopenfilename(
        defaultextension='txt')  # открывает только txt, для docx надо прописать дополнительно
    with open(open_file, 'r') as file:
        text = file.read()
        window_with_text.insert(1.0, text)

    # само окошко, на котором будут вкладки

main = Tk()
main.title('Pl-Fetisowa')
main.geometry('500x300')
main.resizable(height=False, width=False)

# создание самих вкладок
main_frame = ttk.Notebook(main)
task_1, task_2, task_3 = ttk.Frame(main_frame), ttk.Frame(main_frame), ttk.Frame(main_frame)
main_frame.add(task_1, text='Задание №1')
main_frame.add(task_2, text='Задание №2')
main_frame.add(task_3, text='Задание №3')
main_frame.pack(fill='both', expand=True)

# вкладка первая
input_digit1 = Entry(task_1, width=20)
input_digit1.grid(row=1, column=1)

input_sing = Combobox(task_1, width=1)
input_sing['values'] = ('+', '-', '*', '/')
input_sing.grid(row=1, column=2)

input_digit2 = Entry(task_1, width=20)
input_digit2.grid(row=1, column=3)

label_with_answer = Label(task_1, text='= ?????')
label_with_answer.grid(row=1, column=4)

button_to_calculate = Button(task_1, text='Рассчитать', command=calculator_task1)
button_to_calculate.grid(row=1, column=5, sticky='E')  # sticky выравнивание по сторонам света

# вкладка вторая
selector = IntVar()  # сюда приходит значение с нажатой radiobutton(1 или 2 или 3 в int виде, отсюда и IntVar)

radiobutton_1 = Radiobutton(task_2, text='Вариант 1)', value=1, variable=selector)
radiobutton_1.grid(row=1, column=1)

radiobutton_2 = Radiobutton(task_2, text='Вариант 2)', value=2, variable=selector)
radiobutton_2.grid(row=2, column=1)

radiobutton_3 = Radiobutton(task_2, text='Вариант 3)', value=3, variable=selector)
radiobutton_3.grid(row=3, column=1)

what_i_choice = Button(task_2, text='Что я выбрал?', command=radiobutton_task2)
what_i_choice.grid(row=4, column=1)

# вкладка третья
open_file_button = Button(task_3, text='Открыть файл', command=work_with_text_task3)
open_file_button.grid(row=1, column=1, sticky='W')  # sticky выравнивание по сторонам света

window_with_text = scrolledtext.ScrolledText(task_3, width=59, height=15)
window_with_text.grid(row=2, column=1)

# запуск главного окна
main.mainloop()