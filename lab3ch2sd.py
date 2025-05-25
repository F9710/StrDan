#print("Ягодяк Павел Сергеевич АИСа-020303-о24")
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def next_greater_element_linked_list(self):
        current = self.head
        result = []
        stack = []
        index = 0
        
        while current:
            while stack and stack[-1][0] < current.value:
                value, idx = stack.pop()
                result[idx] = current.value
            stack.append((current.value, index))
            result.append(0)
            current = current.next
            index += 1
        
        return result
