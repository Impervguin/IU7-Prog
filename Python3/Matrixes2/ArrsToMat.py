####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
#
####################################################################################################################
import math as m

WALL_SYMB = " "
CEIL_SYMB = " "


nd = int(input("Введите количество элементов в списке D: "))
nf = int(input("Введите количество элементов в списке F: "))
if nd < 1 or nf < 1:
    print("Некорректное значение.")

D = [int(input(f"{i + 1}-й элемент D: ")) for i in range(nd)]  # Ввод списка
F = [int(input(f"{i + 1}-й элемент F: ")) for i in range(nf)]


A = [[m.sin(D[j] + F[k]) for k in range(nf)] for j in range(nd)]

AV = [sum(A[i]) / nf for i in range(nd)]
L = [sum(map(lambda x: x > AV[i], A[i])) for i in range(nd)]



max_elem_len = max(len(str(nf)), len(str(nd))) + 4
for i in range(nd):
    for j in range(nf):
        max_elem_len = max(max_elem_len, len(f"{A[i][j]:.5g}") + 4)

table_length = (max_elem_len + 1) * (nf + 1)
print("Искомая таблица:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(nd)] + [str(el).center(max_elem_len) for el in ["AV", "L"]]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(nd):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [f"{elem:.5g}".center(max_elem_len) for elem in A[i] + [AV[i]] + [L[i]]]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()