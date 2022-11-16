from IntegralMethods import newton, simpson, centered_rects
from PrintMatrix import print_matrix


def f(x):
    return 4 * x ** 3


def primordial_f(x):
    return x ** 4


# Блок ввода
st = float(input("Введите начало отрезка интегрирования: "))
ed = float(input("Введите конец отрезка интегрирования: "))
if st >= ed:
    print("Некорректные значения для начала и конца отрезка.")
    exit()
n1 = int(input("Введите первое количество участков разбиения: "))
if n1 <= 0:
    print("Количество разбиений не может быть отрицательно.")
    exit()
if n1 % 2 != 0:
    print("Число должно делиться на два для работы метода симпсона.")
    exit()
n2 = int(input("Введите второе количество участков разбиения: "))
if n2 <= 0:
    print("Количество разбиений не может быть отрицательно.")
    exit()
if n2 % 2 != 0:
    print("Число должно делиться на два для работы метода симпсона.")
    exit()
# Данный для вывода таблицы
foot = ["Серединных прямоугольников", "Парабол"]
head = [n1, n2]

# Расчет интегралов
l_s1 = simpson(st, ed, n1, f)
l_s2 = simpson(st, ed, n2, f)
l_r1 = centered_rects(st, ed, n1, f)
l_r2 = centered_rects(st, ed, n2, f)
accurate_int = newton(st, ed, primordial_f)

# Вывод таблицы значений интегралов
mat = [
    [f"{l_r1:.5g}", f"{l_r2:.5g}"],
    [f"{l_s1:.5g}", f"{l_s2:.5g}"]
]
print_matrix(mat, head=head, foot=foot, name="Методы Интегральных вычислений")
print(f"Точное значение интеграла по формул Ньютона-Лейбница: {accurate_int:.5g}")

# Расчёт абсолютной погрешности методов
e_s1 = abs(accurate_int - l_s1)
e_s2 = abs(accurate_int - l_s2)
e_r1 = abs(accurate_int - l_r1)
e_r2 = abs(accurate_int - l_r2)

# Расчет относительной погрешности
if accurate_int != 0:
    re_s1 = e_s1 / accurate_int * 100
    re_s2 = e_s2 / accurate_int * 100
    re_r1 = e_r1 / accurate_int * 100
    re_r2 = e_r2 / accurate_int * 100

    e_mat = [
        [f"{e_r1:.5g}, {re_r1:.5g}%", f"{e_r2:.5g}, {re_r2:.5g}%"],
        [f"{e_s1:.5g}, {re_s1:.5g}%", f"{e_s2:.5g}, {re_s2:.5g}%"]
    ]
else:
    e_mat = [
        [f"{e_r1:.5g}, -", f"{e_r2:.5g}, -"],
        [f"{e_s1:.5g}, -", f"{e_s2:.5g}, -"]
    ]
# Вывод таблицы погрешности
print_matrix(e_mat, foot=foot, head=head, name="Погрешности методов")

if min(e_r1, e_r2) > min(e_s1, e_s2):
    print("Метод симпсона оказался точнее при заданных параметрах.")
    simpson_better = True  # Флаг, показывающий более точный метод
else:
    print("Метод срединных прямоугольников оказался точнее при заданных параметрах.")
    simpson_better = False
# Ввод
eps = float(input("Введите точность, до которой нужно довести менее точный метод: "))
max_it = int((input("Введите максимальное количество разбиений: ")))

# Поиск подходящего числа разбиений
for i in range(1, max_it):
    integ = centered_rects(st, ed, i, f) if simpson_better else simpson(st, ed, i, f)
    integ2 = centered_rects(st, ed, 2 * i, f) if simpson_better else simpson(st, ed, 2 * i, f)
    if abs(integ - integ2) < eps:
        break
else:
    print(f"Не удалось достигнуть заданной точности при максимуме в {max_it} разбиений")
    exit()
print(f"{'Метод серединных прямоуольников' if simpson_better else 'Метод парабол'}"
      f" достигает нужной точности при количестве разбиений в {i}")
