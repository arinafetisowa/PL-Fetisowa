#Ввести одномерный массив A длиной m. Поменять в нём местами первый и
#последний элементы. Длину массива и его элементы ввести с клавиатуры. В
#программе описать процедуру для замены элементов массива. Вывести
#исходные и полученные массивы.
def поменятьэлементы(массив):
    if len(массив) > 1:  #проверяем, что массив содержит больше одного элемента
        массив[0], массив[-1] = массив[-1], массив[0]  #vеняем первый и последний элементы
m = int(input("введите длину массива A: "))
A = []
print("введите элементы массива A:")
for i in range(m):
    элемент = float(input(f"элемент {i + 1}: "))
    A.append(элемент)
print("исходный массив A:", A)
#исходный массив вывели
поменятьэлементы(A)
print("полученный массив A:", A)
