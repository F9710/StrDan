
print("Ягодяк Павел Сергеевич АИСа-020303-о24")
def next_greater_element_array(arr):
    n = len(arr)
    result = [0] * n
    stack = []
    
    for i in range(n):
        while stack and arr[stack[-1]] < arr[i]:
            result[stack.pop()] = arr[i]
        stack.append(i)
    
    return result
