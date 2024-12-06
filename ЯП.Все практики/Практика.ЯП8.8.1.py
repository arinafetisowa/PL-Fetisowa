#Задана матрица порядка n и число к. Разделить элементы k-й строки
#на диагональный элемент, расположенный в этой строке.
def divide_row_by_diagonal(matrix, k):
    # Проверяем, что k находится в пределах размерности матрицы
    if k < 0 or k >= len(matrix):
        raise ValueError("Индекс k должен быть в пределах от 0 до n-1, где n - количество строк матрицы.")
# Получаем диагональный элемент в k-й строке
    diagonal_element = matrix[k][k]
# Проверяем, что диагональный элемент не равен нулю
    if diagonal_element == 0:
        raise ValueError("Диагональный элемент равен нулю. Деление на ноль невозможно.")
# Разделяем элементы k-й строки на диагональный элемент
    matrix[k] = [element / diagonal_element for element in matrix[k]]

    return matrix
def input_matrix():
    matrix = []
    print("Введите строки матрицы (по одной строке, разделённой пробелами). Введите 'end' для завершения ввода:")

    while True:
        row_input = input()
        if row_input.lower() == 'end':
            break
        row = list(map(float, row_input.split()))
        matrix.append(row)

    return matrix
#ввод матрицы от руки
matrix = input_matrix()
#ввод индекса строки k
k = int(input("Введите индекс строки k (от 0 до {}): ".format(len(matrix) - 1)))
try:
    result = divide_row_by_diagonal(matrix, k)
    print("Результат:")
    for row in result:
        print(row)
except ValueError as e:
    print(e)