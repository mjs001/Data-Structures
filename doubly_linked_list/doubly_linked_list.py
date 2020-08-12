"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        self.length += 1
        new = ListNode(value)
        if self.head is None:
            self.head = new
            self.tail = self.head
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        self.length -= 1
        v = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return v
        else:
            self.head = self.head.next
            self.head.prev = None
            return v
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        self.length += 1
        new = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        self.length -= 1
        v = self.tail.value
        if self.head is None and self.tail is None:
            return None
        self.tail = self.head = None
        return v    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self. head is None and self.tail is None:
            return None
        elif self.head is self.tail:
            return
        moving_n = node
        moving_n.prev = None
        moving_n.next = self.head
        self.head = moving_n
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        moving_n = node
        if moving_n is self.tail:
            return
        if moving_n is self.head:
            self.remove_from_head()
            self.add_to_tail(moving_n.value)
        else:
            self.delete(moving_n)
            self.add_to_tail(moving_n.value)

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        waste_n = node
        if self.length == 1:
            self.head = self.tail = None
        elif waste_n is self.head:
            self.head = waste_n.next
            self.head.prev = None
        elif waste_n is self.tail:
            self.tail = waste_n.prev
            self.tail.next = None
        else:
            waste_n.prev = waste_n.next
            waste_n.next = waste_n.prev
        self.length -= 1
        return waste_n.value

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pointer = self.head
        highest = self.head.value
        if not self.head:
            return None
        while pointer:
            if pointer.value > highest:
                highest = pointer.value
            pointer = pointer.next
        return highest