quanty_row = int(input('Введите количество строк:'))

input_matrix = []
for i in range(quanty_row):
    row = []
    for i1 in range(quanty_row):
        row.append(int(input('Введите число:')))
    input_matrix.append(row)

print(input_matrix)

output_matrix = []
for i in range(quanty_row):
    new_row = []
    for i1 in range(quanty_row):
        new_row.append(input_matrix[i1][i])
    output_matrix.append(new_row)

print(output_matrix)