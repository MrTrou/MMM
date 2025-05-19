def jacobi_method(a, b, eps=0.1, max_iter=1):
    n = len(b)
    x = [0.0 for _ in range(n)]  # начальное приближение
    for iter_count in range(1, max_iter + 1):
        x_new = x.copy()
        for k in range(n):
            S = sum(a[k][j] * x[j] for j in range(n) if j != k)
            x_new[k] = (b[k] - S) / a[k][k]
        # Проверка условия выхода
        if max(abs(x_new[i] - x[i]) for i in range(n)) < eps:
            print(f'Количество итераций на решение: {iter_count}')
            return x_new
        x = x_new
    return x


# Пример использования:
a = [
    [3, 2, -5],
    [2, -1, 3],
    [1, 2, -1]
]
b = [-1, 13, 9]

solution = jacobi_method(a, b)
print('Решение:', solution)
