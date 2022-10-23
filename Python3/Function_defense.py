# График функции cosx - 1

import math as m

GRAPH_WIDTH = 150
WALL_SYMBOL = "|"
x0, h, xn = [float(i) for i in input("Введите через запятую с пробелом начальное значение, шаг и конечное значение: ").split(", ")]
n_steps = int((xn - x0) / h + 1)
max_y = m.cos(x0) - 1
min_y = m.cos(x0) - 1
max_x_width = 0

for i in range(n_steps):
    x = x0 + h * i
    max_x_width = max(max_x_width, len(f"{x:.5g}"))
    y = m.cos(x) - 1
    max_y = max(y, max_y)
    min_y = min(y, min_y)
y_step = (max_y - min_y) / GRAPH_WIDTH
print(" " * (max_x_width + 1) + f"{min_y:.5g}" + " " * (GRAPH_WIDTH - len(f"{min_y:.5g}")) + f"{max_y:.5g}")
y_zero_pos = int(- min_y / y_step)
for i in range(n_steps):
    x = x0 + h * i
    y = m.cos(x) - 1
    y_pos = int((y - min_y) / y_step)
    if y_zero_pos == y_pos:
        print(f"{x:.5g}".center(max_x_width) + WALL_SYMBOL + " " * y_pos + "*" + " " * (GRAPH_WIDTH - y_pos - 1))
    elif y_zero_pos < y:
        print(f"{x:.5g}".center(max_x_width) + WALL_SYMBOL + " " * y_zero_pos + WALL_SYMBOL + " " * (y_pos - y_zero_pos - 1) + "*" + " " * (GRAPH_WIDTH - y_pos - 1))
    else:
        print(f"{x:.5g}".center(max_x_width) + WALL_SYMBOL + " " * y_pos + "*" + " " * (
                    y_zero_pos - y_pos - 1) + WALL_SYMBOL + " " * (GRAPH_WIDTH - y_zero_pos - 1))


