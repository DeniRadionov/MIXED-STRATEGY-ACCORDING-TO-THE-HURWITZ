import numpy as np
import itertools
def maximize_answer(matrix, l):
    n = len(matrix)
    m = len(matrix[0])
    max_answer = 0.0
    best_p = None
    for p in itertools.product(range(101), repeat=3):
        p1, p2, p3 = p[0] / 100, p[1] / 100, p[2] / 100
        H = np.zeros(m)
        if p1 + p2 + p3 != 1:
            continue
        for i in range(m):
            for j in range(n):
                H[i] += p[j] * matrix[j][i]
        min_H = min(H)
        max_H = max(H)
        answer = round((1 - l) * min_H + l * max_H, 2)
        if answer > max_answer:
            max_answer = answer
            best_p = (p1, p2, p3)
    return best_p

#m = int(input("Введите количество строк: "))
#n = int(input("Введите количество столбцов: "))

#количество строк и столбцов в матрице
m, n=3, 3
matrix = np.zeros((m, n))  # создаем матрицу из нулей

# вводим элементы матрицы
for i in range(m):
    for j in range(n):
        matrix[i][j] = float(input(f"Введите элемент матрицы ({i+1}, {j+1}): "))
print(matrix)

#matrix = [[3, 6, 9], [7, 5, 4], [5, 8, 6]] # test
# заполняем 0
p = np.zeros(m)

l = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]

for k in range(len(l)):
    p = maximize_answer(matrix, l[k])
    H = np.zeros(m)
    for i in range(m):
        for j in range(n):
            H[i] +=matrix[j][i]*p[j]
    print(f'При l={l[k]}:')
    print(f'u({l[k]}) = {min(H)}')
    print(f'U({l[k]}) = {max(H)}')
    print(f'H*({l[k]}) = {round((1-l[k])*min(H)+l[k]*max(H), 3)}\n')
