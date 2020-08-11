"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
class Stack:
    def __init__(self, value):
        self.value = value
        self.next = None
        # self.storage = ?
    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    def remove_head(self):
        if self.head is None and self.tail is None:
            return  
        if not self.head.get_next():
            head = self.headself.head = None
            self.tail = None
            return head.get_value()
        val = self.head.get_value()
        self.head = self.head.get_next()
        return val
    def remove_tail(self):
        if self.head is None and self.tail is None:
            return
        if self.head is self.tail:
            value = self.head.get_value()
            self.head = None
            self.tail = None
            return value
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
            val = self.tail.get_value()
            self.tail = current
            self.tail = current
            self.tail.next = None
            return val
        def contains(self, value):
            if not self.head:
                return False
            current = self.head
            while current:
                if current.get_value() == value:
                    return True
                current = current.get_next()
            return False
        def get_max(self):
            if not self.head:
                return None
            max_value = self.head.get_value()
            current = self.head.get_next()
            while current:
                if current.get_value() > max_value:
                    max_value = current.get_value()
                current = current.get_next()
            return max_value

    class Stack:
        def __init__(self):
            self.size = 0
            self.storage = []
        def __len__(self):
            return len(self.storage)
        def push(self, value):
            self.storage.append(value)
        def pop(self):
            if len(self.storage) > 0:
                return self.storage.pop()
            return None

    class Stack:
        def __init__(self):
            self.size = 0
            self.storage = LinkedList()
        def __len__(self):
            return self.size
        def push(self, value):
            self.storage.add_to_tail(value)
            self.size += 1
        def pop(self):
            if self.size > 0:
                self.size -= 1
                return self.storage.remove_tail()
            return None