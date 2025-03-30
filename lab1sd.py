print("Ягодяк Павел Сергеевич АИСа-020303-о24")
import time
import random
import tracemalloc

N = random.randint(1, 10**6)
print(f"Изначально случайное число N: {N}")
start_time = time.time()
tracemalloc.start()
if N == 0:
    print("no")
else:
    reminder = 0
    for length in range(1, N+1):
        reminder = (reminder * 10 + 1) % N
        if reminder == 0:
            print('1' * length)

            break
    else:
        print("no")

end_time = time.time()
execution_time = end_time - start_time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Время выполнения: {execution_time:.6f} секунд")
print(f"Текущая память: {current / 1024:.2f} КБ")
print(f"Пиковая память: {peak / 1024:.2f} КБ")