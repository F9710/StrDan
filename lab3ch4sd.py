import time
from lab3ch1sd import next_greater_element_array
from lab3ch2sd import LinkedList
from lab3ch3sd import next_greater_element_deque

def test_functions():
    array = [1, 3, 2, 5, 3, 4] * 10000

    # Тест для массива
    start_time = time.time()
    result_array = next_greater_element_array(array)
    end_time = time.time()
    print("Тест для массива:")
    print(result_array[:10])  # Печатаем первые 10 элементов для проверки
    print("Время выполнения (массив):", end_time - start_time)

    # Тест для связанного списка
    linked_list = LinkedList()
    for num in array:
        linked_list.append(num)

    start_time = time.time()
    result_linked_list = linked_list.next_greater_element_linked_list()
    end_time = time.time()
    print("Тест для связанного списка:")
    print(result_linked_list[:10])  
    print("Время выполнения (связанный список):", end_time - start_time)

    # Тест для deque
    start_time = time.time()
    result_deque = next_greater_element_deque(array)
    end_time = time.time()
    print("Тест для deque:")
    print(result_deque[:10])  
    print("Время выполнения (deque):", end_time - start_time)

# Запуск тестов
if __name__ == "__main__":
    test_functions()
