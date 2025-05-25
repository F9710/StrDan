#print("Ягодяк Павел Сергеевич АИСа-020303-о24")
from collections import deque

def next_greater_element_deque(arr):
    n = len(arr)
    result = [0] * n
    stack = deque()
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    
    return result
