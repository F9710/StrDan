print("Ягодяк Павел Сергеевич АИСа-020303-о24")
import numpy as np
import time
from scipy.linalg import blas

# Генерация случайной матрицы комплексных чисел
def generate_complex_matrix(size):
    return np.random.rand(size, size) + 1j * np.random.rand(size, size)

# Вариант 1: Перемножение по формуле из линейной алгебры
#def matrix_multiply_standard(A, B):
    #size = A.shape[0]
    #C = np.zeros((size, size), dtype=np.complex128)
    #for i in range(size):
        #for j in range(size):
            #for k in range(size):
                #C[i, j] += A[i, k] * B[k, j]
    #return C

# Вариант 2: Использование cblas_zgemm
def matrix_multiply_blas(A, B):
    return blas.zgemm(1.0, A, B)

# Вариант 3: Оптимизированный алгоритм (разделение на блоки)
def matrix_multiply_optimized(A, B):
    size = A.shape[0]
    block_size = 64  # Размер блока
    C = np.zeros((size, size), dtype=np.complex128)
    for i in range(0, size, block_size):
        for j in range(0, size, block_size):
            for k in range(0, size, block_size):
                C[i:i+block_size, j:j+block_size] += np.dot(A[i:i+block_size, k:k+block_size], B[k:k+block_size, j:j+block_size])
    return C


def main():
    size = 4096
    A = generate_complex_matrix(size)
    B = generate_complex_matrix(size)

    print("Начинаем перемножение матриц...")

    # Вариант 1
    #print("Вариант 1: Стандартное перемножение...")
    #start_time = time.time()
    #C1 = matrix_multiply_standard(A, B)
    #time_standard = time.time() - start_time
    #c_standard = 2 * size**3
    #p_standard = c_standard / time_standard * 10**-6

    # Вариант 2
    print("Вариант 2: Перемножение с использованием BLAS...")
    start_time = time.time()
    C2 = matrix_multiply_blas(A, B)
    time_blas = time.time() - start_time
    c_blas = 2 * size**3
    p_blas = c_blas / time_blas * 10**-6

    # Вариант 3
    print("Вариант 3: Оптимизированное перемножение...")
    start_time = time.time()
    C3 = matrix_multiply_optimized(A, B)
    time_optimized = time.time() - start_time
    c_optimized = 2 * size**3
    p_optimized = c_optimized / time_optimized * 10**-6


    #print(f"Вариант 1: Время = {time_standard:.6f} сек, Производительность = {p_standard:.2f} MFlops")
    print(f"Вариант 2: Время = {time_blas:.6f} сек, Производительность = {p_blas:.2f} MFlops")
    print(f"Вариант 3: Время = {time_optimized:.6f} сек, Производительность = {p_optimized:.2f} MFlops")

if __name__ == "__main__":
    main()
