x, eps = [float(i) for i in input("Введите x и точность через пробел: ").split()]

if eps > 1:
    print(f"Сумма ряда с точностью до {eps}: {0}")
    exit()
s = 1
i = 1
el = 1 / 2 * x ** 2
while abs(el) > eps:
    print(el)
    s += el
    el *= (-1) * x * x / (2 * i - 1) / (2 * (i + 1))
    i += 1
print(f"Сумма ряда с точностью до {eps}: {s:.7g}")