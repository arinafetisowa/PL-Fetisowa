with open('input.txt', '+r') as file:
    matrix_in_file = file.readlines()
    quanty_row = len(matrix_in_file)

    input_matrix = []
    #запустили цикл по всем  строкам
    for i in range(quanty_row):
        new_row = []
        if i != quanty_row - 1: #чтобы текущая строка была не последеней
            new_row.extend(matrix_in_file[i][:-1][::2])
            input_matrix.append(new_row)
        else:
            new_row.extend(matrix_in_file[i][::2])
            input_matrix.append(new_row)

output_matrix = []
for i in range(quanty_row):
    new_row = []
    for j in range(quanty_row):
        new_row.append(input_matrix[j][i])
    output_matrix.append(new_row)

with open('../output.txt', '+w') as file:
    for i in range(len(output_matrix)):
        row = ''.join(output_matrix[i])
        if i != quanty_row - 1:
            file.write(row + '\n')
        else:
            file.write(row)