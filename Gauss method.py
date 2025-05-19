# Решение системы линейных уравнений методом Гаусса с вычислением определителя

def gauss_method(A, b):
    import copy
    n = len(A)
    # Делаем копии, чтобы не портить исходные данные
    A = copy.deepcopy(A)
    b = copy.deepcopy(b)
    det = 1
    swap_count = 0

    # Прямой ход
    for i in range(n):
        # Поиск максимального элемента для устойчивости (опционально)
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        # Перестановка строк
        if max_row != i:
            A[i], A[max_row] = A[max_row], A[i]
            b[i], b[max_row] = b[max_row], b[i]
            swap_count += 1
        # Приведение к треугольному виду
        for j in range(i + 1, n):
            if A[i][i] == 0:
                det = 0
                continue
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]
    # Вычисление определителя (произведение диагональных элементов)
    for i in range(n):
        det *= A[i][i]
    if swap_count % 2 != 0:
        det *= -1

    # Обратная подстановка
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        sum_ax = 0
        for j in range(i + 1, n):
            sum_ax += A[i][j] * x[j]
        x[i] = (b[i] - sum_ax) / A[i][i]
    return x, det


# Пример использования:
A = [
    [3, 2, -5],
    [2, -1, 3],
    [1, 2, -1]
]
b = [-1, 13, 9]

solution, determinant = gauss_method(A, b)
print("Решение:", solution)
print("Определитель:", determinant)
