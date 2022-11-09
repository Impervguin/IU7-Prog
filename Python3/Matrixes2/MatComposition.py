####################################################################################################################
# Шахнович Дмитрий ИУ7-12Б
#
#
####################################################################################################################
WALL_SYMB = " "
CEIL_SYMB = " "

n, m = map(int, input("Введите через пробел количество строк и столбцов: ").split())
if m <= 0 or n <= 0:
    print("Некорректные размеры матрицы.")
    exit()
max_elem_len = 0
A = [[0] * m for _ in range(n)]
B = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        A[i][j] = int(input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе матрицы A: "))
        max_elem_len = max(len(str(A[i][j])), max_elem_len)
for i in range(n):
    for j in range(m):
        B[i][j] = int(input(f"Введите элемент в {i + 1}-ой строке {j + 1}-ом столбе матрицы B: "))
        max_elem_len = max(len(str(B[i][j])), max_elem_len)

C = [[A[i][j] * B[i][j] for j in range(m)] for i in range(n)]
for i in range(n):
    for j in range(m):
        max_elem_len = max(len(str(C[i][j])), max_elem_len)
V = [sum([C[i][j] for i in range(n)]) for j in range(m)]
max_elem_len += 2
table_length = (max_elem_len + 1) * (m + 1)




print("Матрица A:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(m)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(A[i][j]).center(max_elem_len) for j in range(m)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()

print("Матрица B:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(m)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(B[i][j]).center(max_elem_len) for j in range(m)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print()

print("Матрица C:")
# Шапка таблицы
print(" " * max_elem_len + WALL_SYMB + WALL_SYMB.join([str(i + 1).center(max_elem_len) for i in range(m)]) + WALL_SYMB)
print(CEIL_SYMB * table_length)
for i in range(n):
    # Строки матрицы
    print(str(i + 1).center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
        [str(C[i][j]).center(max_elem_len) for j in range(m)]) + WALL_SYMB)
    print(CEIL_SYMB * table_length)
print("V".center(max_elem_len) + WALL_SYMB + WALL_SYMB.join(
    [str(V[i]).center(max_elem_len) for i in range(m)]) + WALL_SYMB)