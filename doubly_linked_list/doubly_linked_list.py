"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def get_prev(self):
        return self.prev
    
    def set_prev(self, new_prev):
        self.prev = new_prev
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
        new_node = ListNode(value)
        self.length += 1

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node

        else:
            old_head = self.head
            self.head = new_node
            self.head.set_next(old_head)
            old_head.set_prev(self.head)

        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        self.length -= 1

        # If List is empty
        if self.head is None and self.tail is None:
            return
        
        #if List contains a single Node
        elif self.head.get_next() is None:
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()

        else:
            val = self.head.get_next()
            self.head = self.head.get_next()
            self.head.set_prev(None)
            return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        
        # If List is Empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
            
        else:
            old_tail = self.tail
            self.tail.set_next(new_node)
            self.tail = new_node
            self.tail.set_prev(old_tail)


            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.head is None:
            return

        elif self.head is self.tail:
            val = self.tail.get_value()
            self.head = None
            self.tail = None
            self.length -= 1
            return val
        
        else:
            val = self.tail.get_value()
            new_tail = self.tail.get_prev()
            self.tail = new_tail
            self.tail.set_next(None)
            self.length -= 1
            return val
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head is None:
            self.head = node

        else:
            value = node.value
            self.delete(node)
            self.add_to_head(value)

            # previous_val = node.get_prev()
            # next_val = node.get_next()
            # old_head = self.head

            # previous_val.set_next(next_val)
            # next_val.set_prev(previous_val)
            # node.set_prev(None)
            # node.set_next(old_head)
            # self.head = node

        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail is None:
            self.tail = node

        else:
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

            # previous_val = node.get_prev()
            # next_val = node.get_next()
            # old_tail = self.tail

            # previous_val.next = next_val
            # next_val.prev = previous_val
            # node.set_prev(old_tail)
            # node.set_next(None)
            # self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return None

        elif self.head is self.tail:
            self.head = None
            self.tail = None
            self.length -= 1
        
        elif self.head is node:
            node.next.set_prev(None)
            self.head = node.next
            self.length -= 1

        elif self.tail is node:
            node.prev.set_next(None)
            self.tail = node.prev
            self.length -= 1

        else:
            self.length -= 1
            if node.prev:
                node.prev.set_next(node.next)
            if node.next:
                node.next.set_prev(node.prev)
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None:
            return None
        
        else:
            max_value = self.head.get_value()
            current = self.head.get_next()
            while current is not None:
                if current.get_value() > max_value:
                    max_value = current.get_value()
                current = current.get_next()
            return max_value